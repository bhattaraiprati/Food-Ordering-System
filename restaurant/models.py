from django.db import models

# Create your models here.
class Restaurant(models.Model):
    res_id = models.IntegerField(unique= True, primary_key= True)
    res_name = models.CharField(max_length=200)
    owner_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    # menu_upload = models.FileField(upload_to="menus/")
    def __str__(self) -> str:
        return self.res_name

class menu_list(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    menu = models.CharField(max_length=100)


class User(models.Model):
    name = models.CharField(max_length=100)
    

    

