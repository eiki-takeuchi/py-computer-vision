"""restframework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, routers
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
import os
import sys

dir = os.getcwd()
head, tail = os.path.split(dir)
sys.path.append(head)

from gcp import image_annotation as ia

# Serializers define the API representation.
# - Serializer is similar to Form and ModelForm in Django. 
# - Serializers converts complex data and model into native Python data types. 
# - This is a replacement of Model in usual django usage. 
# Official Documentation
# https://www.django-rest-framework.org/api-guide/serializers/
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False)
    def vision_api(self, request, format=None):

        image_uri = request.query_params["url"]

        client = ia.vision_client()
        response = ia.annotate_image(vision_client=client, image_uri=image_uri)
        result = ia.extract_top_confidences(response, num=5, display=False)

        return Response(result)


# Routers provide a way of automatically determining the URL conf.
# # Check url patterns with command-line.
# $ ./manage.py show_urls sss
router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename="users")


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

