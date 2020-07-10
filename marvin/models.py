import os
from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    link = models.CharField(max_length=200)
    image = models.ImageField(upload_to='marvin/project_images/projects', blank=True, null=True)
    started_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title