# WebCroller
Very Simple WebCroller

tag : 긁어올 태그, att : 긁어올 속성, parser : 파서의 종류
# get_html(url ,tag ,attributes ,parser)


 example --------------------
# url = 'http:// ----- '

# print(get_html(url,'table',{'class':'test1'},'html5lib'))

print(get_html(url,0,0,'html5lib'))
print(get_html(url,'table',0,'html5lib'))

