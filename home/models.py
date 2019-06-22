from django.db import models

# Create your models here.

class Home(models.Model):
    purpose = models.TextField('建站目的')

    class Meta:
        verbose_name = '首页说明'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.purpose