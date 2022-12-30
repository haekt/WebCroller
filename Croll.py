import get_html
url='https://www.codeit.kr/community/threads/19938'

print(get_html.get_html(url,'table',{'class':'test1'},'html5lib'))
