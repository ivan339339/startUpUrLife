from django.template import Template, Context

def generateHtml(user, parsed):
    mainTemplate='''
    <html>
    
    <head>
    <style type="text/css">
            * { margin: 0; padding: 0; }
            body { font: 16px Helvetica, Sans-Serif; line-height: 24px; background: url(images/noise.jpg); }
            .clear { clear: both; }
            #page-wrap { width: 1200px; margin: 40px auto 60px; }
            h1 { margin: 0 0 16px 0; padding: 0 0 16px 0; font-size: 42px; font-weight: bold; letter-spacing: -2px; border-bottom: 1px solid #999; }
            h2 { font-size: 20px; margin: 0 0 6px 0; position: relative; }
            h2 span { position: absolute; bottom: 0; right: 0; font-style: italic; font-family: Georgia, Serif; font-size: 16px; color: #999; font-weight: normal; }
            p { margin: 0 0 16px 0; }
            #objective { width: 500px; float: left; }
            #objective p { font-family: Georgia, Serif; font-style: italic; color: #666; }
            dt { font-style: italic; font-weight: bold; font-size: 18px; text-align: right; padding: 0 26px 0 0; width: 100px; float: left; height: 100px; border-right: 1px solid #999;  }
            dd { width: 400 px; float: left; margin: 0 20}
            dd.clear { float: none; margin: 0; height: 15px; }
         </style>
    </head>
    
    <body>
    
    <div id="page-wrap">
    
    <h1 class='fn'>{{ FullName }}</h1>
    
    <div id="objective">
            <p>
                    Born on {{ BirthDate }}
            </p>
    </div>
    
    <dl>
            <dd class="clear"></dd>
    
            <dt>Portfolio</dt>
            <dd>
                    {{ PortfolioTemplate }}
            </dd>
            
            <dd class="clear"></dd>
                
            <dt>Residence</dt>
            <dd>
                <p>{{ Residence }}</p>
            </dd>
            
            <dd class="clear"></dd>
                
            <dt>Adress</dt>
            <dd>
                <p>{{ Address }}</p>
            </dd>
                
        </dl>
    </div>
    </body>
    </html> '''    
    
    portfolioTemplate = ''
    for key in parsed:
        portfolioTemplate += '''<h2>''' + key + '''</h2>\n'''
        portfolioTemplate += '''<p>''' + parsed[key] + '''</p>\n'''
    ans = Template(mainTemplate)
    context = Context({"FullName": user.FullName,
                    "BirthDate": user.BirthDate,
                    "Residence": user.Residence,
                    "Address": user.Address,
                    "PortfolioTemplate": portfolioTemplate})

    return ans.render(context)
