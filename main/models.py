from django.db import models
import math

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=200, unique=True)
    flight_cost = models.IntegerField()
    photo = models.ImageField(upload_to="images/", blank=True)
    food_cost = models.IntegerField()

    def __str__(self):
        return self.name

    def cost_of_day(self, num_people):
        hotel = self.hotel_set.get(num_beds=num_people)
        result = hotel.night_cost  + self.food_cost

        return result

    def get_affordable_days(self, num_people, budget):
        hotel = self.hotel_set.get(num_beds=num_people)
        day_cost = hotel.night_cost  + self.food_cost
        result = budget / day_cost

        return math.floor(result)

    def get_entertaiment_categoryes(self):
        set = []
        ens = self.entertaiment_set.all()
        for e in ens:
            for c in e.category.all():
                set.append(c.category_title)
        return set

class Category(models.Model):
    category_title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.category_title


class Entertaiment(models.Model):
    title = models.CharField(max_length=200)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    cost = models.IntegerField()
    photo = models.ImageField(upload_to="images/", blank=True)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title


ROOMS = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
)

class Hotel(models.Model):
    title = models.CharField(max_length=200)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    night_cost = models.IntegerField()
    num_beds = models.IntegerField(choices=ROOMS, verbose_name="For how many people: ", default=1)
    photo1 = models.ImageField(upload_to="images/", blank=True, verbose_name="Image 1")
    photo2 = models.ImageField(upload_to="images/", blank=True, verbose_name="Image 2")
    photo3 = models.ImageField(upload_to="images/", blank=True, verbose_name="Image 2")

    def __str__(self):
        return self.title

