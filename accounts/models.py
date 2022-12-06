from django.db import models
from django.utils import timezone
from django.utils.timezone import localtime
from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Audio(models.Model):
    date_created = models.DateTimeField(default=timezone.now(), blank=False)
    file = CloudinaryField(resource_type='video',null=True, blank=True, folder='kin-keepers/')
    message  = CloudinaryField(resource_type='raw',null=True,folder='transcriptions/')
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self) -> str:
        return str(self.file)
