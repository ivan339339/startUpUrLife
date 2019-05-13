from tastypie.resources import ModelResource

from app.models import *

class UserByIdResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user/'
        list_allowed_methods = ['get']
