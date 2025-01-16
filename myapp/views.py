from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Food, Supplements, CaloriesBurnt, Consume

@login_required
def index(request):
    if request.method == "POST":
        # Fetch the selected items as lists from the form
        foods_consumed = request.POST.getlist('foods_consumed[]')  # Handle multiple foods
        supplements_consumed = request.POST.getlist('supplements_consumed[]')  # Handle multiple supplements
        calorie_spent = request.POST.get('calorie_spent')  # Single calorie-burnt entry

        # Process foods
        for food_name in foods_consumed:
            food = Food.objects.filter(name=food_name).first()  # Retrieve Food object
            if food:  # Check if food exists
                Consume.objects.create(user=request.user, food_consumed=food)

        # Process supplements
        for supplement_name in supplements_consumed:
            supplement = Supplements.objects.filter(name=supplement_name).first()  # Retrieve Supplement object
            if supplement:  # Check if supplement exists
                Consume.objects.create(user=request.user, supplement_consumed=supplement)

        # Process calories burnt
        if calorie_spent:
            calorie = CaloriesBurnt.objects.filter(name=calorie_spent).first()  # Retrieve CaloriesBurnt object
            if calorie:  # Check if calorie entry exists
                Consume.objects.create(user=request.user, calorie_burnt=calorie)

        # Redirect to the same page to prevent form resubmission
        return redirect('index')  # Replace 'index' with your URL pattern name

    # Fetch data for the dropdowns and the consumed list
    consumed_food = Consume.objects.filter(user=request.user)
    foods = Food.objects.all()
    supplements = Supplements.objects.all()
    calorie_burnt = CaloriesBurnt.objects.all()

    # Render the template with context
    return render(request, 'myapp/index.html', {
        'consumed_food': consumed_food,
        'foods': foods,
        'supplementss': supplements,
        'calorie_burnt': calorie_burnt
    })
