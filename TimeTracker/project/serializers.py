from . import models
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):

    class Meta:

        model = models.Task
        fields = ("task",)


class ProjectSerializer(serializers.ModelSerializer):

    task = TaskSerializer(read_only=True, many=True)
    print(task)
    class Meta:

        model = models.Project
        fields = ("id", "project_name", "task",)
        print(fields)
