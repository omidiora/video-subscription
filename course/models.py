from django.db import models
from django.urls import reverse
from membership.models import Membership

class Courses(models.Model):
    slug=models.SlugField()
    title=models.CharField(max_length=120)
    description=models.TextField()
    allowed_meberships=models.ManyToManyField(Membership)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('courses  :detail',kwarg={'slug':self.slug})

class Lesson(models.Model):
    slug=models.SlugField()
    title=models.CharField(max_length=120)
    course=models.ForeignKey(Courses,on_delete=models.SET_NULL,null=True)
    position=models.IntegerField()
    video_url=models.CharField(max_length=200)
    thumbnail=models.ImageField()

    def __str__(self):
        return self.title
     
