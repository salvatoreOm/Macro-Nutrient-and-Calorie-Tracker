from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Food, Supplements, CaloriesBurnt, Consume

@login_required
def index(request):
    if request.method == "POST":
        # Fetch the selected items from the form
        food_consumed = request.POST.get('foods_consumed')  # Single food selection
        supplement_consumed = request.POST.get('supplements_consumed')  # Single supplement selection
        calorie_spent = request.POST.get('calorie_spent')  # Single calorie-burnt entry

        # Process food
        consumeF = Food.objects.filter(name=food_consumed).first() if food_consumed else None
        # Process supplement
        consumeS = Supplements.objects.filter(name=supplement_consumed).first() if supplement_consumed else None
        # Process calories burnt
        burntCal = CaloriesBurnt.objects.filter(name=calorie_spent).first() if calorie_spent else None

        # Create a single entry with all the data
        if consumeF or consumeS or burntCal:
            Consume.objects.create(
                user=request.user,
                food_consumed=consumeF,
                supplement_consumed=consumeS,
                calorie_burnt=burntCal
            )

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


def delete_consume(request, id):
    if request.method == 'POST':
        consumed_food = Consume.objects.get(id=id, user=request.user)
        consumed_food.delete()
        return redirect('index') 
    return render(request,'myapp/delete.html')
