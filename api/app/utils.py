from django.template import Template, Context

def generateHtml(user, parsed, template):
    portfolioTemplate = ''
    for key in parsed:
        portfolioTemplate += '''<h2>''' + key + '''</h2>\n'''
        portfolioTemplate += '''<p>''' + parsed[key] + '''</p>\n'''
        
    template = template
    ans = Template(template)
    context = Context({"FullName": user.FullName,
                    "BirthDate": user.BirthDate,
                    "Residence": user.Residence,
                    "Address": user.Address})

    return ans.render(context)
