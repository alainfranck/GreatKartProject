from django.db import models
from django.db.models import Avg, Count
from django.urls import reverse

from category.models import Category
from accounts.models import Account
from multiselectfield import MultiSelectField

class Product(models.Model):
    product_name = models.TextField(blank=True)
    reference = models.CharField(max_length=200, null=True, blank=True)
    sous_titre = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    information = models.TextField(blank=True)
    livraison = models.CharField(max_length=200, null=True, blank=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name

    def average_review(self):
        reviews = ReviewRating.objects.filter(product=self, status=True).aggregate(average=Avg('rating'))
        avg = 0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
        return avg

    def count_review(self):
        reviews = ReviewRating.objects.filter(product=self, status=True).aggregate(count=Count('id'))
        count = 0
        if reviews['count'] is not None:
            count = int(reviews['count'])
        return count

    def is_variation(self):
        is_var = False
        if self.variation_set.count() > 0:
            is_var = True
        return is_var


class VariationManager(models.Manager):

    def supports(self):
        return super(VariationManager, self).filter(variation_category='support', is_active=True)

    def details(self):
        return super(VariationManager, self).filter(variation_category='detail', is_active=True)

    def dimensions(self):
        return super(VariationManager, self).filter(variation_category='dimension', is_active=True)


variation_category_choise = (
        ('support', 'support'),
        ('detail', 'detail'),
        ('dimension', 'dimension'),
    )


class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=100, choices=variation_category_choise)
    variation_value = models.CharField(max_length=100)
    # extra_price = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_date = models.DateField(auto_now=True)

    objects = VariationManager()

    def __str__(self):
        return f'{self.variation_value} ({self.variation_category})'


class VariationPrice(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variations = models.ManyToManyField(Variation, related_name='variationprice', null=True, blank=True)
    price = models.IntegerField(default=0)
    created_date = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.product.product_name} | Variation price'


class ReviewRating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject


class ProductGallery(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='store/products/', max_length=255)

    def __str__(self):
        return self.product.product_name

    class Meta:
        verbose_name = 'productgallery'
        verbose_name_plural = 'product gallery'
