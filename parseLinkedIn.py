import re, json, os
from bs4 import BeautifulSoup

def parsePage(filename):
  with open(filename, 'rb') as f:
      p = f.read().decode('utf8', 'ignore')

  p = p.replace('&lt;','<').replace('&gt','>').replace('&quot;','"').replace('&amp;','&').replace('&#61;','=') #.replace('>','>\n')

  # with open('file.html', 'w', encoding='utf8') as f:
  #     f.write(p)

  soup = BeautifulSoup(p,'lxml')
  data = soup.select('code')
  data = coo.text.replace('\n','')
  return json.loads(data)
