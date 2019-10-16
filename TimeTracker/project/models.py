from django.db import models


class Project(models.Model):
    project_name = models.CharField(max_length=200)
    task = models.ManyToManyField('Task')

    def __str__(self):
        return self.project_name


class Task(models.Model):
    task = models.CharField(max_length=200)

    def __str__(self):
        return self.task


