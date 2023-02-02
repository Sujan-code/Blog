#from pyexpat import model
#from tkinter import CASCADE
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here. auto_now=true=jahile update garyo tei hunxa
#auto_now_add=true create gareko date


class Post(models.Model):
    CATEGORY = (
			('Politics', 'Politics'),
			('Travel', 'Travel'),
            ('Automation', 'Automation'),
			('History', 'History'),
            ('Technology', 'Technology'),
    )

    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now,blank=True,null=True)
    author = models.ForeignKey(User , on_delete=models.CASCADE,blank=True,null=True)
    category = models.CharField(max_length=200, null=True,blank=True,choices=CATEGORY)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

