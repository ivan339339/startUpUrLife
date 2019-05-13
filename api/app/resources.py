from tastypie.resources import ModelResource, ALL
from tastypie.authentication import BasicAuthentication

from app.models import *

class UserByIdResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['Password']
        allowed_methods = ['get']
        filtering = {
            'Login' : ALL,
            'Password' : ALL
        }