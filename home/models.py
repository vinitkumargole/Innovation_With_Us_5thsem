import email
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    message = models.TextField()
    date = models.DateField()    

    def __str__(self):
        return self.name


class idea(models.Model):


    Category_Choice = (
    ('ent','Entrepreneur'),
    ('inv', 'Investor'),
    )
   
    Country_Choice = (
    ('ind','India'),
    ('ch', 'China'),
    ('uk', 'U.K.'),
    )

    name = models.CharField(max_length=122)
    mobile = models.IntegerField()
    category = models.CharField(
        max_length = 20,
        choices = Category_Choice,
        default = 'ent'
        )
    profit = models.IntegerField()
    lastname = models.CharField(max_length=122)
    email = models.EmailField(max_length=122)
    valuation = models.CharField(max_length=122)
    companyname = models.CharField(max_length=122)
    country= models.CharField(
        max_length = 20,
        choices = Country_Choice,
        default = 'Ind'
        )
    file= models.ImageField(upload_to="profile_pic/",null=True ,default='profile_pic/default.jpg')
    message = models.TextField()
    date = models.DateField()    