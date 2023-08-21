from multiprocessing import context
from django.shortcuts import render
from . models import Guide, Secusigne
from orders.models import Order
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def get_orders(request):
    order_list = Order.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(order_list, 10)
    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)
    context = {
        'orders': orders,

    }
    return render(request, 'orders/orders_.html', context)

def vente(request):
    return render(request, 'store/vente.html')

def promotion(request):
    return render(request, 'store/promotion.html')

def catalogue(request):
    return render(request, 'store/catalogue.html')

def chimique(request):
    return render(request, 'store/chimique.html')
    
def obligation(request):
    return render(request, 'store/obligation.html')
    
    
def interdiction(request):
    return render(request, 'store/interdiction.html')
    
def faq(request):
    return render(request, 'store/faq.html')

def danger(request):
    return render(request, 'store/danger.html')


def detailSecusigne(request, slug):
    context = {}
    try:
        blog_obj = Secusigne.objects.filter(slug=slug).first()
        context['blog_obj'] = blog_obj
    except Exception as e:
        print(e)
    return render(request, 'store/detail_secusigne.html', context)

def guide(request):
    guides = Guide.objects.all()
    context = {
        'guides': guides,
    }
    return render(request, 'store/guide.html', context)

def detailGuide(request, slug):
    context = {}
    try:
        blog_obj = Guide.objects.filter(slug=slug).first()
        context['blog_obj'] = blog_obj
    except Exception as e:
        print(e)
    return render(request, 'store/detail_guide.html', context)
    
    
    
def habitation(request):
    return render(request, 'store/habitation.html')
    
def bureau(request):
    return render(request, 'store/bureau.html')    
    
def commerce(request):
    return render(request, 'store/commerce.html')
    
def hotel(request):
    return render(request, 'store/hotel.html')
    
def entrepot(request):
    return render(request, 'store/entrepot.html') 
    
def chantier(request):
    return render(request, 'store/chantier.html') 
    
def hopital(request):
    return render(request, 'store/hopital.html') 
    
def ecole(request):
    return render(request, 'store/ecole.html') 
    
