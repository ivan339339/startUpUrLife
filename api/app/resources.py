from tastypie.resources import ModelResource, ALL
from tastypie.authorization import Authorization
from django.http import HttpResponse


from app.models import *

class UserByIdResource(ModelResource):
    def get_list(self, request, **kwargs):
        resp = super(UserByIdResource, self).get_list(request, **kwargs)
        data = json.loads(resp.content)
        if len(data['objects']) == 0:
            data['errors'] = 'AttributeError - no such user with this login-password.'
        data = json.dumps(data)
        return HttpResponse(data, content_type='application/json', status=200)

    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['Password']
        allowed_methods = ['get', 'post', 'put', 'delete']
        filtering = {
            'Login' : ALL,
            'Password' : ALL
        }


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
