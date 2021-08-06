from django.contrib import admin
from django import forms
from .models import Category, Product, RatingStar, Rating
from django.utils.safestring import mark_safe

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(label='Опис', widget=CKEditorUploadingWidget())

    class Meta:
        model = Product
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_image')
    list_display_links = ('name',)
    readonly_fields = ('get_image', )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="60" height="60"')

    get_image.short_description = "Зображення"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'category', 'description', 'price', 'availability', 'get_image')
    list_filter = ('category', )
    search_fields = ('product_name', 'category__name')
    form = ProductAdminForm
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="60" height="60"')

    get_image.short_description = "Зображення"


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('star', 'product', 'ip')


admin.site.register(RatingStar)

admin.site.site_header = "Агромагазин"

