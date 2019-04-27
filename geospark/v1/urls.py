from django.conf.urls import url
from rest_framework_mongoengine import routers as merouters
from geospark.v1.views import ToolViewSet

merouter = merouters.DefaultRouter()
merouter.register(r'mongo', ToolViewSet)

urlpatterns = [

]

urlpatterns += merouter.urls