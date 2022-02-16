from django.contrib import admin
from .forms import ColorForm
from .models import *
 
# @admin.register(Image)

class ImageInline(admin.TabularInline):
	model = Image
	raw_id_fields = ['product']
	# list_display = ['product', 'image_description', 'created']
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

	list_display = ['name', 'unit_price', 'short_description', 'category', 'created', 'status']
	ist_filter = ['status', 'created', 'updated']
	inlines = [ImageInline]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'created']

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):

	list_display = ['size_name']
	
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

	list_display = ['user', 'product', 'text', 'created']


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
	form = ColorForm
	# filter_horizontal = ('color_name',)
	fieldsets = (
	    (None, {
	        'fields': (('color_name',), 'color_code')
	        }),
	    )
	list_display = ['color_name', 'color_code']


# admin.site.register(Image, ImageInline)
# admin.site.register(Product, ProductAdmin)
# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Size, SizeAdmin)
# admin.site.register(Review, ReviewAdmin)
# admin.site.register(Color, ColorAdmin)