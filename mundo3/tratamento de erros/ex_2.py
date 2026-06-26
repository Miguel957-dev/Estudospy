#site pudim
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br/')
except urllib.error.URLError:
    print('Não foi possivel acessar o site no momento.')
else:
    print('Conseguir acessar o site.')
    print(site.read())