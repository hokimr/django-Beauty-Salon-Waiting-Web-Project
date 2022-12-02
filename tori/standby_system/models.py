from cProfile import label
from unicodedata import name
from django.db import models
from django import forms

# Create your models here.
class waiting(models.Model):
    Surgery_CHOICES = (
    ('커트','커트' ),
    ('펌', '펌'),
    ('매직','매직')
)
    designer_CHOICES = (
    ('제시','제시' ),
    ('가을', '가을'),
    ('소리','소리'),
    ('은정','은정'),
    ('다은','다은'),
    ('미지정','미지정')
)

    designer = models.CharField(verbose_name='디자이너 선택',max_length=10,null=False,choices=designer_CHOICES)
    name = models.CharField(verbose_name='대기자 이름',max_length=10,null=False)
    Surgery = models.CharField(verbose_name='시술 선택',max_length=10, null=False,choices=Surgery_CHOICES)
    #  models.CharField(max_length=10,null=False)


    def __str__(self):
        return f"{self.name} {self.Surgery}"