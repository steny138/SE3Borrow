from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from home import settings
from sim.models import Sim

class Borrower(models.Model):
    """docstring for Borrow"""
    no = models.AutoField(primary_key=True)
    author = models.ForeignKey(User)
    sim = models.ForeignKey(Sim)
    
    borrowType = models.CharField(max_length=10, null=True)
    reason = models.CharField(max_length=1100, null=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    borrow_date = models.DateTimeField(null=True)
    published_date = models.DateTimeField(
            blank=True, null=True)

    class Meta:
        db_table = 'Borrower'

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
        