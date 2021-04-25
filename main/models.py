from django.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=200, unique=True)
    flight_cost = models.IntegerField()
    photo = models.ImageField(upload_to="images/", blank=True)
    food_cost = models.IntegerField()
    #entertaiment = models.ForeignKey(Entertaiment, on_delete=models.CASCADE)
    #hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

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

