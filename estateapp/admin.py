from django.contrib import admin

# Register your models here.
from .models import Item
from .models import *

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Filter_Price)
admin.site.register(contactEnquiry)

