from django.db import models

# Create your models here.
NEWSLETTER_OPTION = [
    ('M','Monthly'),
    ('W','Weekly')
]

class Subscribe(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100,unique=True)
    option = models.CharField(max_length=1,choices=NEWSLETTER_OPTION,default='M')


