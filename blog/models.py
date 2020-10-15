from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Post(models.Model):  # w nawiasie po czym dziedziczy klasa(model)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self): # to jest funkcja przekierowujaca na edytowany post po edytowaniu lub stworzeniu nowego
        return reverse('post-detail', kwargs={'pk': self.pk})

