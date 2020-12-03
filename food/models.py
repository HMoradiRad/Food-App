from django.db import models

# Create your models here.

class Item(models.Model):

    def __str__(self):
        return self.item_name


    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500,default="https://lh3.googleusercontent.com/proxy/unDY-PdQ2dcEOe8nfIq7xgtLm1lAGEO9Nb3-ZBJwF7Z48CPL5bgAu_5HraSrW2o4gbT6OWYZDc0Oj4i6WHRVjZiSbqB8x9onRfVHjNUvrNnmtQhC4doVa2UZ4iq2x50")
