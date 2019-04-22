from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from cart.models import Cart


class Features(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=100, default="")
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    views = models.IntegerField(default=0)
    purchased_feature = models.IntegerField(default=0)
    upvotes = models.IntegerField(default=0)
    price_of_feature = models.DecimalField(max_digits=6, decimal_places=2)
    # Todo, Pending, Completed
    status = models.CharField(max_length=254, default='Todo')
    cart = models.ManyToManyField(Cart)

    def __str__(self):
        return self.title


class FeatureComments(models.Model):
    user = models.ForeignKey(User)
    comments = models.TextField()
    features = models.ForeignKey(Features)

    def __str__(self):
        return self.comments