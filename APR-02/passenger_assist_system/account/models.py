from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=32)
    author = models.CharField(max_length=64)
    pages = models.IntegerField()
    price = models.FloatField()
    is_new = models.BooleanField(default=False)
    created = models.DateField()

    def __str__(self):
        return self.name

"""

Architecture
MVC: Model View Controller

Django follows MVT: Model View Template architecture

1) Break / Continue / Pass
2) Date time 
3) While Loop
4) If and else endif
5) Database, HW: Should learn about DELETE/WHERE/UPDATE/INSERT/SELECT and custom FIELDS
6) Models are tables 
7) python manage.py makemigrations and python manage.py migrate
8) Admin panel


"""