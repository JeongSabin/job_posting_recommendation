from django.db import models

# Create your models here.

# 게시글(Post)엔 제목(postname), 내용(contents)이 존재합니다

class post3(models.Model):
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