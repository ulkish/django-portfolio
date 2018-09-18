from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='project', blank=True)
    link = models.CharField(max_length=50,  default='Project link.')
    github_link = models.CharField(max_length=50, default='Github link.')



    def __str__(self):
        return '{}'.format(self.name)
