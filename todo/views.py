from rest_framework.viewsets import ModelViewSet
from .serializers import Todo,Todo_seriazlizer

class Todo_view(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = Todo_seriazlizer
    