from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ReviewRating, ProductGallery, Variation, VariationPrice
from .forms import ReviewForm
from category.models import Category
from carts.models import CartItem
from orders.models import OrderProduct
from carts.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def store(request, category_slug=None):
    categories = None
    products = None
    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        paginator = Paginator(products, 10)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    else:
        # mostra apenas produtos disponiveis e os ordena pelo id
        products = Product.objects.all().filter(is_available=True).order_by('id')
        paginator = Paginator(products, 10)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    context = {'products': paged_products,
               'product_count': product_count,
               }
    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        # verifica se o item esta no carrinho
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
    except Exception as e:
        raise e
    if request.user.is_authenticated:
        try:
            orderproduct = OrderProduct.objects.filter(user=request.user, product_id=single_product.id).exists()
        except OrderProduct.DoesNotExist:
            orderproduct = None
    else:
        orderproduct = None

    #     pega as reviews
    reviews = ReviewRating.objects.filter(product_id=single_product.id, status=True)

    # product gallery
    product_gallery = ProductGallery.objects.filter(product_id=single_product.id)
    related_products = Product.objects.filter(category=single_product.category).exclude(id = single_product.id)

    # variation price management

    support_chose = request.GET.get('support', '')
    detail_chose = request.GET.get('detail', '')
    dimension_chose = request.GET.get('dimension', '')

    if support_chose is not '' or detail_chose is not '' or dimension_chose is not '':
        variation_prices = VariationPrice.objects.filter(product__id=single_product.id)
        print(variation_prices)
        for vari_price in variation_prices:
            print([v.variation_value for v in vari_price.variations.all()])
            var_list = [v.variation_value for v in vari_price.variations.all()]
            var_chose_combinaison = []

            if support_chose is not '':
                var_chose_combinaison.append(support_chose)
            if detail_chose is not '':
                var_chose_combinaison.append(detail_chose)
            if dimension_chose is not '':
                var_chose_combinaison.append(dimension_chose)


            print(var_chose_combinaison)

            if var_chose_combinaison == var_list or support_chose in var_list and detail_chose in var_list and dimension_chose in var_list:
                single_product.price = vari_price.price

    context = {'single_product': single_product,
               'in_cart': in_cart,
               'support_chose': support_chose,
               'detail_chose': detail_chose,
               'dimension_chose': dimension_chose,
               'orderproduct': orderproduct,
               'reviews': reviews,
               'product_gallery': product_gallery,
               'related_products': related_products,}


    return render(request, 'store/product_detail.html', context)


def search(request):
    products = {}
    product_count = 0
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword)
                                                                        | Q(product_name__icontains=keyword))
            product_count = products.count()
    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)


def submit_review(request, product_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            reviews = ReviewRating.objects.get(user__id=request.user.id, product__id=product_id)
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            messages.success(request, 'Thanks! Your review been updated')
            return redirect(url)
        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.product_id = product_id
                data.user_id = request.user.id
                data.save()
                messages.success(request, 'Thanks! Your review been submitted')
                return redirect(url)
