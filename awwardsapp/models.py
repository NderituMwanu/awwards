from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime
# Create your models here.


STATUS = (
            (0,"Draft"),
            (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length = 30, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    slug = models.SlugField(max_length=200, default="")
    updated_on = models.DateTimeField(auto_now= True) 
    created_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    location = models.CharField(max_length =20, unique= True, default='World')
    rating = models.IntegerField(validators=[MinValueValidator(0),          
                                            MaxValueValidator(5)])
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(upload_to='media/')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True)
    bio =models.CharField(max_length = 30, unique=True)
    updated_on =  models.DateTimeField(auto_now= True)
    image = models.ImageField(upload_to='media/', default= 'default.jpg')

    def __str__(self):
        return self.user.username
