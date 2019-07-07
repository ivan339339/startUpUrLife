from django.template import Template, Context
from app.templates import *

def generateHtml(user, parsed, style):
    portfolioTemplate = ''
    for key in parsed:
        portfolioTemplate += '''<h2>''' + key + '''</h2>\n'''
        portfolioTemplate += '''<p>''' + parsed[key] + '''</p>\n'''
        
    template = formatting.format(styles[style], user.FullName, user.BirthDate, portfolioTemplate, user.Residence, user.Address)
    ans = Template(template)
    context = Context({"FullName": user.FullName,
                    "BirthDate": user.BirthDate,
                    "Residence": user.Residence,
                    "Address": user.Address})

    return ans.render(context)
