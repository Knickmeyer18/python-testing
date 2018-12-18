#urllib module practice


import urllib.request

html = urllib.request.urlopen('https://arstechnica.com').read()
print(html)

