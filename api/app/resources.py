from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.authorization import Authorization
from django.forms.models import model_to_dict
from django.http import HttpResponse
from app.utils import generateHtml
import pdfkit
from tastypie import fields
from datetime import date
import json


from app.models import *

class UserByIdResource(ModelResource):
    def obj_create(self, bundle, request=None, **kwargs):
        bundle.data['RegistrationDate'] = '{0}-{1}-{2}'.format(date.today().year, date.today().month, date.today().day)
        bundle = super(UserByIdResource, self).obj_create(bundle)

        id = bundle.obj
        Portfolio.objects.create(UserID=id, Title='', Text='')

        return bundle

    class Meta:
        queryset = User.objects.all()
        always_return_data = True
        resource_name = 'users'
        allowed_methods = ['get', 'post', 'put']
        authorization = Authorization()


class UserAuth(ModelResource):
    def post_list(self, request, **kwargs):
        self.method_check(request, allowed=['post'])
        data = self.deserialize(request, request.body, format=request.META.get('CONTENT_TYPE', 'application/json'))

        login = data.get('Login', '')
        password = data.get('Password', '')

        user = User.objects.all().filter(Login=login, Password=password).first()

        if user is None:
            data = {'error': 'AttributeError - no user found with this login-password'}
            return self.create_response(request, data, status=404)
        else:
            data = model_to_dict(user)
            return self.create_response(request, data)

    class Meta:
        queryset = User.objects.all()
        resource_name = 'user/auth'
        allowed_methods = ['post']
        authorization = Authorization()

class PortfolioByIdResource(ModelResource):
    UserID = fields.ForeignKey(UserByIdResource, attribute="UserID")

    class Meta:
        queryset = Portfolio.objects.all()
        resource_name = 'portfolios'
        allowed_methods = ['get', 'put', 'post']
        filtering = {
            'UserID': ALL
        }
        authorization = Authorization()


class GoalByIdResource(ModelResource):
    UserID = fields.ForeignKey(UserByIdResource, attribute="UserID")

    class Meta:
        queryset = Goal.objects.all()
        resource_name = 'goals'
        allowed_methods = ['get', 'post', 'put']
        filtering = {
            'UserID' : ALL
        }
        authorization = Authorization()

class AppointementsByUserIdResource(ModelResource):
    UserID = fields.ForeignKey(UserByIdResource, attribute="UserID")

    class Meta:
        queryset = Appointement.objects.all()
        resource_name = 'appointments'
        allowed_methods = ['get', 'post', 'put']
        filtering = {
            'UserID': ALL
        }
        authorization = Authorization()

class PortfolioInPdf(ModelResource):
    def create_response(self, bundle, data, response_class=HttpResponse, **kwargs):
        super(PortfolioInPdf, self).create_response(bundle, data, response_class, **kwargs)
        id = bundle.GET['UserID']
        style = bundle.GET['Style']
        user = User.objects.all().filter(UserID=id).first()
        portfolios = Portfolio.objects.all().filter(UserID=id).all()

        portfolio = {}

        for p in portfolios:
            portfolio[p.Title] = p.Text

        html = generateHtml(user, portfolio, style)

        pdf = pdfkit.from_string(html, False)

        filename = "cv.pdf"

        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="' + filename + '"'
        return response

    class Meta:
        queryset = Portfolio.objects.all()
        resource_name = 'portfolio/download'
        allowed_methods = ['get']
        filtering = {
            'UserID': ALL
        }
        authorization = Authorization()

class HelpResource(ModelResource):
    class Meta:
        queryset = Help.objects.all()
        resource_name = 'help'
        allowed_methods = ['post','get']
        authorization = Authorization()