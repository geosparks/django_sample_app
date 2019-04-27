from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
 
from rest_framework_mongoengine import viewsets as meviewsets
from geospark.v1.serializers import ToolSerializer
from geospark.v1.models import Tool
 
class ToolViewSet(meviewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer