from django.db import models
from django.utils.translation import gettext as _
# Create your models here.

class develop_manager_data(models.Model):
    category = models.CharField(max_length=2000)
    page_url = models.CharField(max_length=2000)
    picture_url = models.CharField(max_length=2000)
    title = models.CharField(max_length=2000)
    company = models.CharField(max_length=2000)
    work = models.CharField(max_length=2000)
    qualification = models.CharField(max_length=2000)
    favor = models.CharField(max_length=2000)
    welfare = models.CharField(max_length=2000)
    skill_stack = models.CharField(max_length=2000)
    place = models.CharField(max_length=2000)
    money = models.CharField(max_length=2000)
    employee = models.CharField(max_length=2000)
    first_cleaned_welfare = models.CharField(max_length=2000)
    first_cleaned_works = models.CharField(max_length=2000)
    scaler_money = models.CharField(max_length=2000)
    def __str__(self):
        return self.title