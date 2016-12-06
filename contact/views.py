from django.shortcuts import render


from .models import Contact
from rest_framework import viewsets
from .Serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
	queryset = Contact.objects.all().order_by('-created')
	serializer_class = TaskSerializer

