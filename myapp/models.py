from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Food(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    carbs = models.FloatField()
    protein = models.FloatField()
    fats = models.FloatField()
    calories = models.IntegerField()
  

class Supplements(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    carbs = models.FloatField()
    protein = models.FloatField()
    fats = models.FloatField()
    calories = models.IntegerField()


class CaloriesBurnt(models.Model):

    def __str__(self):
        return self.name if self.name else "Unnamed"

    name = models.CharField(max_length=100)
    caloriesburnt= models.IntegerField()


class Consume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE, null=True, blank=True)
    supplement_consumed = models.ForeignKey(Supplements, on_delete=models.CASCADE, null=True, blank=True)
    calorie_burnt = models.ForeignKey(CaloriesBurnt, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - Food: {self.food_consumed}, Supplement: {self.supplement_consumed}, Calories Burnt: {self.calorie_burnt}"

