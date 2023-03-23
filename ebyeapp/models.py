from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


# Create your models here.
class Categ(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    img = models.ImageField(upload_to='category_images')
    priority = models.IntegerField()

    class Meta:
        ordering = ('priority',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def get_url(self):
        return reverse('category', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    img = models.ImageField(upload_to="product_images")
    desc = models.TextField()
    price = models.IntegerField()
    mrp = models.IntegerField()
    stock = models.IntegerField()
    available = models.BooleanField()
    categ = models.ForeignKey(Categ, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def get_url(self):
        return reverse('details', args=[self.categ.slug, self.slug])

    def __str__(self):
        return '{}'.format(self.name)
