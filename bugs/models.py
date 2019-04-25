from django.db import models
from django.contrib.auth.models import User


class Bugs(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    views = models.IntegerField(default=0)
    upvotes = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images',blank=True)
    # Todo, Pending, Completed
    status = models.CharField(max_length=254, default='Todo')

    def __str__(self):
        return self.name


class Comments(models.Model):
    bug_id = models.ForeignKey(Bugs, on_delete=models.DO_NOTHING)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    comment = models.CharField(max_length=254)

    def __str__(self):
        return self.bug_id