from django.db import models

from django.contrib.auth.models import User
from django.db.models.fields import PositiveIntegerField



class Publisher(models.Model) :
    name=models.CharField(max_length=255)
    detail=models.TextField()
    address=models.TextField()
    def __str__(self):
        return(self.name)
    

LANGUAGE_CHOICES = (("en", "English"), ("hi", "Hindi"))


# Create your models here.
class Books(models.Model) :
    title=models.CharField(max_length=255)
    subtitle=models.CharField(max_length=255,null=True,blank=True)
    detail=models.TextField()
    mrp=models.PositiveIntegerField()
    discount=models.PositiveIntegerField()
    pages=models.PositiveIntegerField()
    languages=models.CharField(choices=LANGUAGE_CHOICES,default='en',max_length=255)
    pub_date=models.DateField()
    publisher=models.ForeignKey(Publisher,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    img=models.ImageField(upload_to='books',null=True,blank=True)

    def __str__(self):
        return self.title

class Bookauthors(models.Model):
    book=models.ForeignKey(Books,on_delete=models.CASCADE)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self) :
        return self.book.title +' '+ self.author.username
        #return f"{self.book.title} {self.book.author.username}"






