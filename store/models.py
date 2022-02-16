from django.db import models
from django.urls import reverse
from users.models import User
from django.utils.translation import gettext_lazy as _



STATUS_CHOICES = (('notavailable', 'Notavailable'),('available', 'Available'),)
RATING_CHOICES = ((1, "★☆☆☆☆"), (2, "★★☆☆☆"), (3, "★★★☆☆"), (4, "★★★★☆"), (5, "★★★★★"))

class AvailableManager(models.Manager):
	def get_queryset(self):
		return super(AvailableManager, self).get_queryset() .filter(status='available')


class Category(models.Model):
	name = models.CharField(max_length=200, db_index=True)
	description = models.TextField(null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	
	class Meta:
		ordering = ('name',)
		verbose_name = 'category'
		verbose_name_plural = 'categories'
	
	def __str__(self):
		return self.name
	

	# def get_absolute_url(self):
	# 	return reverse('store:product_list_by_category', args=[self.slug])


class Size(models.Model):
	SIZELIST = (('SMALL', '0 - 3 months'),
				('MEDIUM', '3 - 6 months'),
				('LARG', '6 - 12 months'),
				('XLARG', '12 - 18 months'),

				)
	# size = models.CharField(choices=SIZELIST, max_length=21)
	size_code = models.CharField(max_length = 100 , null = True , blank = True)
	size_name = models.CharField(max_length = 50 , null = True , blank = True )

	def __str__(self):
		return self.size_name

class Color(models.Model):

	color_code = models.CharField(max_length = 50 , null = True , blank = True)
	color_name = models.CharField(max_length = 50 , null = True , blank = True )

	def __str__(self):
		return self.color_name




	color_of = {
		'#000000': 'black',
		'#ffffff': 'white',
		'#808080': 'dark gray',
		'#b0b0b0': 'light gray',
		'#ff0000': 'red',
		'#800000': 'dark red',
		'#00ff00': 'green',
		'#008000': 'darkgreen',
		'#0000ff': 'blue',
		'#000080': 'dark blue',
		'#ffff00': 'yellow',
		'#808000': 'olive',
		'#00ffff': 'cyan',
		'#ff00ff': 'magenta',
		'#800080': 'purple',
		'#FFC0CB': 'pink',
		'#FF10F0': 'neon pink',
	}

	@staticmethod
	def get_color_name(hx):
	# if color is found in dict
	    if colorof.has_key(hx):return colorof[hx]

	    # else return its closest available color
	    m = 16777215
	    k = '000000'
	    for key in colorof.keys():
	        a = int(hx[:2],16)-int(key[:2],16)
	        b = int(hx[2:4],16)-int(key[2:4],16)
	        c = int(hx[4:],16)-int(key[4:],16)

	        v = a*a+b*b+c*c # simple measure for distance between colors

	        # v = (r1 - r2)^2 + (g1 - g2)^2 + (b1 - b2)^2

	        if v <= m:
	            m = v
	            k = key

	    return colorof[k]

	


class Image(models.Model):

	product = models.ForeignKey(to = 'Product', null=False, default=1, on_delete=models.CASCADE )
	image = models.ImageField(upload_to='products/%Y/%m/%d',null=True, blank=True)
	image_description = models.CharField(max_length = 999, null = True , blank = True)
	color = models.ManyToManyField(to = Color, related_name = 'image_color')
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	
	@staticmethod
	def get_all_product_img(product_id):
		if product_id:
			return Image.objects.filter(product=product_id)
		else:
			return None


class Product(models.Model):

	def upload_thumb_dir(self, filename):
		path = f'productsimg/{self.brand}/%Y/%m/%d/{filename}'
		return path



	name = models.CharField(max_length=200, db_index=True)
	brand = models.CharField(max_length = 100 , null = True , blank = True)
	category = models.ForeignKey(to = Category, related_name='products', on_delete=models.CASCADE)
	short_description = models.TextField(blank=True)
	unit_price = models.DecimalField(max_digits=10, decimal_places=2)
	discount_price = models.FloatField(blank=True, null=True)
	status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='notavailable')
	available_quantity = models.PositiveIntegerField(null = True , blank = True)
	thumbnail = models.ImageField(upload_to = upload_thumb_dir, null=True)
	color = models.ManyToManyField(to = Color, related_name = 'product_color')
	size = models.ManyToManyField(to = Size, related_name = 'product_size')
	features = models.TextField(blank=True, null=True)
	rating = models.PositiveIntegerField(choices=RATING_CHOICES, blank=True, null=True)
	
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	

	class Meta:
		ordering = ('-created', 'name', )

	def __str__(self):
		return self.name

	def get_rating_percentage(self):
		return self.rating * 20 if self.rating is not None else None

	@staticmethod
	def get_products_by_id(ids):
		return Product.objects.filter(id__in=ids)

	@staticmethod
	def get_available_products():
		return Product.available.all()

	@staticmethod
	def get_all_products():
		return Product.objects.all()

	@staticmethod
	def get_all_products_by_category(category_id):
		if category_id:
			return Product.objects.filter(category=category_id)
		else:
			return Product.get_all_products()


	objects = models.Manager() # The default manager.
	available = AvailableManager() # Our custom manager.



class Review(models.Model):
	product = models.ForeignKey(to = Product, on_delete=models.CASCADE)
	user = models.ForeignKey(to = User, on_delete=models.CASCADE)
	text = models.TextField('Review Text')

	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'{self.user} on {self.product}'