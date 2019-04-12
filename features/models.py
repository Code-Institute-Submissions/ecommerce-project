from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class features(models.Model):
    title = models.CharField(max_length=100, default="")
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    views = models.IntegerField(default=0)
    purchased_feature = models.IntegerField(default=0)
    upvotes = models.IntegerField(default=0)
    price_of_feature = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title


class featurecomments(models.Model):
    comments = models.TextField()
    features = models.ForeignKey(features)

    def __str__(self):
        return self.comments