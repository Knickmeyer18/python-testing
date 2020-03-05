#urllib module practice


import urllib.request

url_list = ['https://signin.acorns.com/present']

#html = urllib.request.urlopen('https://signin.acorns.com/present').read()
html = urllib.request.urlopen(url_list[0]).read()
print(html)

