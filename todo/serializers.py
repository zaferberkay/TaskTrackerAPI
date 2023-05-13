from rest_framework import serializers
from .models import Todo

class Todo_seriazlizer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        # fields = '__all__'
        exclude = [
            'created_date',
            'updated_date',
        ]
