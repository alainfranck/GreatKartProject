from django.contrib import admin
from .models import Product, Variation, ReviewRating, ProductGallery, VariationPrice
import admin_thumbnails
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.utils.text import (
    capfirst, format_lazy, get_text_list, smart_split, unescape_string_literal,
)
from django_summernote.admin import SummernoteModelAdmin


@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1


class VariationAdminInline(admin.TabularInline):
    model = Variation
    extra = 1


class ProductAdmin(SummernoteModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category',
                    'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}
    inlines = [ProductGalleryInline, VariationAdminInline]
    summernote_fields = ('description','information',)


class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category',
                    'variation_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('product', 'variation_category',
                   'variation_value', 'is_active')


@admin.register(VariationPrice)
class VariationPriceAdmin(admin.ModelAdmin):
    list_display = ('product', 'get_variations', 'price')
    list_editable = ('price',)
    list_filter = ('variations',)

    def get_variations(self, obj):
        return " | ".join([v.variation_value for v in obj.variations.all()])


admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)
admin.site.register(ReviewRating)
admin.site.register(ProductGallery)