from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.CharField(max_length=255,)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.text +' , '+ str(self.user)+' , '+ str(self.created_at) +' , '+ str(self.updated_at)

    def get_absolute_url(self):
        return reverse('post-list')