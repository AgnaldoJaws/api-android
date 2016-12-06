from rest_framework import serializers
from .models import Contact

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'name', 'lastname', 'email', 'companyName', 'telephone')


