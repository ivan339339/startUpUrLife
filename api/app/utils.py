from django.template import Template, Context

def generateHtml(user, parsed):
    mainTemplate = '''
    <html>
    <body>

    <h3>{{ FullName }}</h3>

    <ul>
        <p>Birth date: {{ BirthDate }}</p>

        <dt>Residence</dt>
        <dd>{{ Residence }}</dd>

        <br>

        <dt>Address</dt>
        <dd>{{ Address }}</dd>

    </ul>

    <h3>Portfolio</h3>

    <ol>

        {{ PortfolioTemplate }}

    </ol>

    </body>
    </html> '''

    portfolioTemplate = ''
    for key in parsed:
        portfolioTemplate += "<li>" + parsed[key] + "</li>\n"
    ans = Template(mainTemplate)
    context = Context({"FullName": user.FullName,
                       "BirthDate": user.BirthDate,
                       "Residence": user.Residence,
                       "Address": user.Address,
                       "PortfolioTemplate": portfolioTemplate})

    return ans.render(context)