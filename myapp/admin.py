from django.contrib import admin
from .models import Food
from .models import Supplements
from .models import CaloriesBurnt
# Register your models here.
admin.site.register(Food)
admin.site.register(Supplements)
admin.site.register(CaloriesBurnt)
