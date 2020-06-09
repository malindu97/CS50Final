import os
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from vote.models import VoteModel

# from django.core.files.storage import FileSystemStorage


# Create your models here.
class images(VoteModel, models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    description =  models.CharField(max_length=200)
    date = models.CharField(max_length=64, null=True, blank=True)
    picture = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"{self.userid} - {self.id} - {self.date}"
    
    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.picture.name))
        super(images,self).delete(*args,**kwargs)