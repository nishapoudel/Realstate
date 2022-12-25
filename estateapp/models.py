from distutils.command.upload import upload
from email import message
from email.policy import default
from time import timezone
from django.db import models
from django.urls import  reverse
from datetime import datetime

# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length=100)
    slug=models.SlugField(unique=True)


    class Meta:
        ordering=('-name',)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('estateapp:item_by_category', args=[self.slug])    #appname:urlname

class Filter_Price(models.Model):
    FILTER_PRICE = (
       ('Less than 50 Lacs', 'Less than 50 Lacs'),
       ('50 Lacs - 1 Crore ', '50 Lacs - 1 Crore '),
       ('1 Crore - 3 Crores', '1 Crore - 3 Crores'),
       ('3 Crores - 5 Crores', '3 Crores - 5 Crores'),
       ('5 Crores - 10 Crores', '5 Crores - 10 Crores'),
       ('10 Crores - 100 Crores', '10 Crores - 100 Crores'),
    )
    price = models.CharField(choices= FILTER_PRICE, max_length=100)
    def __str__(self):
        return self.price

class contactEnquiry(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    message = models.CharField(max_length=150)
    class Meta:
        ordering=('-name',)
    def __str__(self):
        return self.name

class Item(models.Model):

    name = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    area= models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, default=1)
    filter_price = models.ForeignKey(Filter_Price, on_delete=models.CASCADE, null=True, default='50 lakhs')
    slug = models.CharField(max_length=100, default= 'real-state' )

    price = models.IntegerField()
    image = models.ImageField(upload_to = 'image/', default=1 )

    created_date = models.DateField(default=datetime.now)


    class Meta:
        ordering=('-name',)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
       return reverse('estateapp:item_detail',args=[self.id,])

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url=''
        return url




