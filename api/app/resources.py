from tastypie.resources import ModelResource, ALL
from tastypie.authorization import Authorization
from django.forms.models import model_to_dict
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
        allowed_methods = ['get', 'post', 'put']
        authorization = Authorization()


        def hydrate(self, bundle):
            bundle.request.data['RegistrationDate'] = '{0}-{1}-{2}'.format(date.today().year, date.today().month, date.today().day)
            return bundle

class UserAuth(ModelResource):
    def post_list(self, request, **kwargs):
        self.method_check(request, allowed=['post'])
        data = self.deserialize(request, request.body, format=request.META.get('CONTENT_TYPE', 'application/json'))

        login = data.get('Login', '')
        password = data.get('Password', '')

        user = User.objects.all().filter(Login=login, Password=password).first()

        if user is None:
            data = {'error': 'AttributeError - no user found with this login-password'}
            data = json.dumps(data)
            return self.create_response(request, data)
        else:
            data = model_to_dict(user)
            data = json.dumps(data, default=str)
            return self.create_response(request, data)

    class Meta:
        queryset = User.objects.all()
        resource_name = 'user/auth'
        allowed_methods = ['post']
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
