from django.db import models
from django.contrib.auth.models import User


class Cart(models.Model):
    user = models.ForeignKey(User)
    total_amount = models.IntegerField(default=0)

    def __str__(self):
        return 'Cart - ' + str(self.user)

    def save(self, *args, **kwargs):
        if Cart.objects.filter(user=self.user):
            return "Constraint: One Cart per User"
        super(Cart, self).save(*args, **kwargs)