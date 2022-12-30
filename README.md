# WebCroller
Very Simple Python WebCroller


# get_html(url ,tag ,attributes ,parser)
tag : Types of Tags to Import, att : Attributes to import, parser : type of parser

 # example --------------------
 url = 'http:// ----- '

 print(get_html(url,'table',{'class':'test1'},'html.parser'))

 print(get_html(url,0,0,'html5lib'))
 
 print(get_html(url,'table',0,'html5lib'))

