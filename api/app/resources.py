from tastypie.resources import ModelResource, ALL
from tastypie.authorization import Authorization

from app.models import *

class UserByIdResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['Password']
        allowed_methods = ['get', 'post', 'put', 'delete']
        filtering = {
            'Login' : ALL,
            'Password' : ALL
        }
        authorization = Authorization()

class PortfolioByIdResource(ModelResource):
    class Meta:
        queryset = Portfolio.objects.all()
        resource_name = 'portfolio'
        allowed_methods = ['get', 'post', 'put', 'delete']
        authorization = Authorization()


class GoalByIdResource(ModelResource):
    class Meta:
        queryset = Goal.objects.all()
        resource_name = 'goal'
        allowed_methods = ['get', 'post', 'put', 'delete']
        authorization = Authorization()

class AppointementsByUserIdResource(ModelResource):
    class Meta:
        queryset = Appointement.objects.all()
        resource_name = 'appointment'
        allowed_methods = ['get', 'post', 'put', 'delete']
        authorization = Authorization()
        
