formatting = '''
<html>

<head>
<style type="text/css">
        {0}
     </style>
</head>

<body>
<div id='header'></div>
<div id="page-wrap">

<h1 class='fn'>{1}</h1>

<div id="objective">
	<p>
		Born on {2}
	</p>
</div>

<dl>
	<dd class="clear"></dd>

	<dt>Portfolio</dt>
	<dd>
		 {3}
	</dd>
	
        <dd class="clear"></dd>
            
        <dt>Residence</dt>
        <dd>
            <p>{4}</p>
        </dd>
        
        <dd class="clear"></dd>
            
        <dt>Address</dt>
        <dd>
            <p>{5}</p>
        </dd>
            
    </dl>
</div>
</body>
</html> '''

styles = {
    'default' : '''* { margin: 0; padding: 0; }
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
            #header { height: 50px; }''',
    'blue' : '''* { margin: 0; padding: 0; }
        body { font: 16px Helvetica, Sans-Serif; line-height: 24px; background: url(images/noise.jpg); }
        .clear { clear: both; }
        #page-wrap { width: 1200px; margin: 40px auto 60px; }
        h1 { margin: 0 0 16px 0; padding: 0 0 16px 0; font-size: 42px; font-weight: bold; letter-spacing: -2px; border-bottom: 1px solid #999; color: #04859D}
        h2 { font-size: 20px; margin: 0 0 6px 0; position: relative; color: #04859D}
        h2 span { position: absolute; bottom: 0; right: 0; font-style: italic; font-family: Georgia, Serif; font-size: 16px; color: #999; font-weight: normal; }
        p { margin: 0 0 16px 0; }
        #objective { width: 500px; float: left; }
        #objective p { font-family: Georgia, Serif; font-style: italic; color: #666; }
        dt { font-style: italic; font-weight: bold; font-size: 18px; text-align: right; padding: 0 26px 0 0; width: 100px; float: left; height: 100px; border-right: 1px solid #999;  color: #37B6CE; }
        dd { width: 400 px; float: left; margin: 0 20}
        dd.clear { float: none; margin: 0; height: 15px; }
        #header { height: 50px; }''',
    'green' : '''* { margin: 0; padding: 0; }
        body { font: 16px Helvetica, Sans-Serif; line-height: 24px; background: url(images/noise.jpg); }
        .clear { clear: both; }
        #page-wrap { width: 1200px; margin: 40px auto 60px; }
        h1 { margin: 0 0 16px 0; padding: 0 0 16px 0; font-size: 42px; font-weight: bold; letter-spacing: -2px; border-bottom: 1px solid #999; color: #9BF33D; }
        h2 { font-size: 20px; margin: 0 0 6px 0; position: relative; color: #9BF33D; }
        h2 span { position: absolute; bottom: 0; right: 0; font-style: italic; font-family: Georgia, Serif; font-size: 16px; color: #999; font-weight: normal; }
        p { margin: 0 0 16px 0; }
        #objective { width: 500px; float: left; }
        #objective p { font-family: Georgia, Serif; font-style: italic; color: #666; }
        dt { font-style: italic; font-weight: bold; font-size: 18px; text-align: right; padding: 0 26px 0 0; width: 100px; float: left; height: 100px; border-right: 1px solid #999;  color: #D0F86F; }
        dd { width: 400 px; float: left; margin: 0 20}
        dd.clear { float: none; margin: 0; height: 15px; }
        #header { height: 50px; }'''
}
