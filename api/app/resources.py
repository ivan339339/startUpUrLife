from tastypie.resources import ModelResource, ALL
from tastypie.authorization import Authorization
from django.http import HttpResponse
from datetime import date


from app.models import *

class UserByIdResource(ModelResource):
    def obj_create(self, bundle, request=None, **kwargs):
        bundle.data['RegistrationDate'] = '{0}-{1}-{2}'.format(date.today().year, date.today().month, date.today().day)
        bundle = super(UserByIdResource, self).obj_create(bundle)
        return bundle

    class Meta:
        queryset = User.objects.all()
        resource_name = 'users'
        excludes = ['Password']
        allowed_methods = ['get', 'post', 'put']
        authorization = Authorization()


        def hydrate(self, bundle):
            bundle.request.data['RegistrationDate'] = '{0}-{1}-{2}'.format(date.today().year, date.today().month, date.today().day)
            return bundle

class UserAuth(ModelResource):
    def get_list(self, request, **kwargs):
        resp = super(UserAuth, self).get_list(request, **kwargs)

        data = resp.content

        if not isinstance(resp.content, bytes):
            if len(data['objects']) == 0:
                data['errors'] = 'AttributeError - no such user with this login-password.'
            data = json.dumps(data)

        return HttpResponse(data, content_type='application/json', status=200)

    class Meta:
        queryset = User.objects.all()
        resource_name = 'users/auth'
        excludes = ['Password']
        allowed_methods = ['put']
        filtering = {
            'Login' : ALL,
            'Password' : ALL
        }
        authorization = Authorization()

class PortfolioByIdResource(ModelResource):
    class Meta:
        queryset = Portfolio.objects.all()
        resource_name = 'portfolio'
        allowed_methods = ['get', 'put', 'post']
        authorization = Authorization()


class GoalByIdResource(ModelResource):
    class Meta:
        queryset = Goal.objects.all()
        resource_name = 'goals'
        allowed_methods = ['get', 'post', 'put']
        authorization = Authorization()

class AppointementsByUserIdResource(ModelResource):
    class Meta:
        queryset = Appointement.objects.all()
        resource_name = 'appointments'
        allowed_methods = ['get', 'post', 'put']
        authorization = Authorization()
