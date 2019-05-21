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

class PortfolioByIdResource(ModelResource):
    class Meta:
        queryset = Portfolio.objects.all()
        resource_name = 'portfolio'
        allowed_methods = ['get']


class GoalByIdResource(ModelResource):
    class Meta:
        queryset = Goal.objects.all()
        resource_name = 'goal'
        allowed_methods = ['get']

class AppointementsByUserIdResource(ModelResource):
    class Meta:
        queryset = Appointement.objects.all()
        resource_name = 'appointement'
        allowed_methods = ['get']
        
