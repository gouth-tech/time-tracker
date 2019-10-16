from django.urls import path
from project.views import ProjectView, TaskView

app_name = 'project'

urlpatterns = [
    path('users/projects/', ProjectView.as_view(), name="project"),
    path('users/tasks/<int:pk>/', TaskView.as_view(), name="task"),


]
