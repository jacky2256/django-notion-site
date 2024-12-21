from rest_framework.generics import CreateAPIView
from .models import ExampleModel
from .serializers import ExampleModelSerializer
from rest_framework.permissions import AllowAny


class ExampleModelCreateView(CreateAPIView):
    queryset = ExampleModel.objects.all()
    serializer_class = ExampleModelSerializer
    permission_classes = [AllowAny]
