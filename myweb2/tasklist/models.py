from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(upload_to='uploads/avatars/', null=True, blank=True)

class Category(models.Model):
    name = models.CharField(max_length=200)

class Course(models.Model):
    subject = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/courses/', null=True, blank=True)
    create_dates = models.DateTimeField(auto_now_add=True)
    update_dates = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='courses')

class Lesson(models.Model):
    subject = models.CharField(max_length=200, null=False)
    content = RichTextField()
    image = models.FileField(upload_to='uploads/lessons/', default=None)
    create_dates = models.DateTimeField(auto_now_add=True)
    update_dates = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    tags = models.ManyToManyField('Tag', related_name='lessons')

class Tag(models.Model):
    name = models.CharField(max_length=200)
