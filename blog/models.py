from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    item = models.CharField(max_length=100)
    price = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    person = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.item
