from django.db import models

# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=50)
    author=models.CharField(max_length=40)
    isbn=models.PositiveIntegerField()
    publisher=models.CharField(max_length=30)

    def __str__(self):
        return str(self.name)+"["+str(self.isbn)+']'


       