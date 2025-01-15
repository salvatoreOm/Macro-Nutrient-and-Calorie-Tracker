from django.contrib import admin
from .models import Food,Supplements,CaloriesBurnt,Consume
# Register your models here.
admin.site.register(Food)
admin.site.register(Supplements)
admin.site.register(CaloriesBurnt)
admin.site.register(Consume)
