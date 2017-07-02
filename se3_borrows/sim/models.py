
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.db import models

from home import settings

class Sim(models.Model):
    # author = models.ForeignKey(User)
    sim_id = models.AutoField(primary_key=True)
    number = models.CharField(max_length=20, null=False, default='No Number')
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    operate = models.CharField(max_length=10, null=True, choices=settings.OPERATE_CHOICES)
    status = models.CharField(max_length=2, null=True, choices=settings.STATUS_CHOICES)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    class Meta:
        db_table = 'SimCards'

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title