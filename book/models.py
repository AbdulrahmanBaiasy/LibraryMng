from django.db import models

# Create your models here.


class Category (models.Model): 
    name = models.CharField( max_length=50)

    def __str__(self):
        return self.name 

class Book (models.Model): 

    status_book = [
        ('available', 'available'), 
        ('rented', 'rented'),
        ('sold', 'sold')
    ]

    title = models.CharField( max_length=50)
    author = models.CharField (max_length = 50 , null = True  , blank = True)
    photo_book = models.ImageField (upload_to = 'photos', null = True  , blank = True )
    photo_author = models.ImageField (upload_to = 'photos', null = True , blank = True )  
    price = models.DecimalField (max_digits = 5 , null = True,decimal_places = 2 , blank = True )
    pages = models.IntegerField (null = True , blank = True )
    rental_price_day = models.DecimalField (max_digits = 5 ,null = True, decimal_places = 2, blank = True  )
    rental_duration = models.IntegerField (null = True , blank = True )
    rental_total = models.DecimalField (max_digits = 5 ,null = True, decimal_places = 2, blank = True  )
    active = models.BooleanField (default = True , blank = True )
    status = models.CharField(max_length = 50 , choices = status_book, null = True  , blank = True)
    category = models.ForeignKey (Category, on_delete = models.PROTECT , null = True , blank = True )

    def __str__(self):
        return self.title 
    