from django.shortcuts import render
from .models import Hotel, Entertaiment, Category, Place

# Create your views here.
def home(request):
    categoryes = Category.objects.all()

    ctx = {'categoryes': categoryes} 

    return render(request, 'main/home.html', ctx)


def algorithm(request):
    budget = request.POST.get('budget')
    num_people = request.POST.get('num_people')
    category = request.POST.get('category')
    # print(type(budget))
    # print(num_people)
    # print(category)
    places = Place.objects.all()
    set = []
    for p in places:
        try: 
            int(budget) - (p.flight_cost * int(num_people)) > 3 * p.cost_of_day(int(num_people))
            set.append(p)
        except:
            print("Error has been caught!")

    # print(place.get_affordable_days(num_people, int(budget)))

    for p in set:
        if category not in p.get_entertaiment_categoryes():
            set.pop(set.index(p))
            # print(category)
        # print(p.get_entertaiment_categoryes())

    ctx = {
        "set": set,
    }

    return render(request, 'main/results.html', ctx)

def detail_view(request, place_name):
    place = Place.objects.get(name=place_name)
    entertaiments = place.entertaiment_set.all()
    hotels = place.hotel_set.all()
    hotel = hotels[0]

    ctx = {
       'place': place,
       'entertaiments': entertaiments, 
       'hotels': hotels,
       'hotel': hotel,
    }

    return render(request, 'main/detail.html', ctx)
    