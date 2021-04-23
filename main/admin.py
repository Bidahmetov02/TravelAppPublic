from django.contrib import admin
from .models import Hotel, Category, Place, Entertaiment
# Register your models here.
admin.site.register(Hotel)
admin.site.register(Category)
admin.site.register(Place)
admin.site.register(Entertaiment)

