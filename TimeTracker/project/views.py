from project.serializers import ProjectSerializer
from rest_framework.generics import RetrieveAPIView, ListAPIView
from .models import Project
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response


class TaskView(RetrieveAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectSerializer

    def get_object(self):

        return Response(data=Project.objects.get(pk=self.kwargs.get('pk')),
                        status=status.HTTP_200_OK)


class ProjectView(ListAPIView):

    permission_classes = ()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        print(self.request.session['users'])
        return Project.objects.all()


