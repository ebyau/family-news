from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.



class Document(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=200)
    created_by = models.CharField(max_length=50,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
