from django.urls import path
from .views import ExampleModelCreateView

urlpatterns = [
    path('example/', ExampleModelCreateView.as_view(), name='example-create'),
]
