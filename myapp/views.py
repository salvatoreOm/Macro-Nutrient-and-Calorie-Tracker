from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Food, Supplements, CaloriesBurnt, Consume
#create your views here.

@login_required  # Ensures only authenticated users can access this view
def index(request):
    if request.method == "POST":
        food_consumed = request.POST.get('food_consumed')  # Use `get` to avoid KeyError
        supplement_consumed = request.POST.get('supplement_consumed')
        calorie_spent = request.POST.get('calorie_spent')

        try:
            # Fetch objects from the database
            consumeF = Food.objects.get(name=food_consumed) if food_consumed else None
            consumeS = Supplements.objects.get(name=supplement_consumed) if supplement_consumed else None
            burntCal = CaloriesBurnt.objects.get(name=calorie_spent) if calorie_spent else None

            # Create and save a single Consume entry
            Consume.objects.create(
                user=request.user,
                food_consumed=consumeF,
                supplement_consumed=consumeS,
                calorie_burnt=burntCal
            )
        except (Food.DoesNotExist, Supplements.DoesNotExist, CaloriesBurnt.DoesNotExist) as e:
            # Handle invalid inputs gracefully
            return render(request, 'myapp/index.html', {
                'foods': Food.objects.all(),
                'supplementss': Supplements.objects.all(),
                'calorie_burnt': CaloriesBurnt.objects.all(),
                'error': str(e)
            })

    # Fetch data for the form
    foods = Food.objects.all()
    supplementss = Supplements.objects.all()
    calorie_burnt = CaloriesBurnt.objects.all()

    # Render the template with the required data
    return render(request, 'myapp/index.html', {
        'foods': foods,
        'supplementss': supplementss,
        'calorie_burnt': calorie_burnt
    })
