#!C:\Users\User\AppData\Local\Programs\Python\Python39\python.exe

import os
import urllib.parse
import sys
from bs4 import BeautifulSoup
import requests 

def enc_print(string='', encoding='utf8'):
    sys.stdout.buffer.write(string.encode(encoding) + b'\n')


def slugfy(slug):
    slug = slug.lower()
    slug = slug.replace(" ", "-")
    slug = slug.replace('à', 'a')
    slug = slug.replace('á', 'a')
    slug = slug.replace('ã', 'a')
    slug = slug.replace('â', 'a')
    slug = slug.replace('é', 'e')
    slug = slug.replace('í', 'i')
    slug = slug.replace('ó', 'o')
    slug = slug.replace('ô', 'o')
    slug = slug.replace('ú', 'u')
    slug = slug.replace('(*)', '')
    return slug

    
enc_print("Content-Type: text/html; charset=utf-8\n")
query_dict = urllib.parse.parse_qs(os.environ['QUERY_STRING'])
        

estado = str(query_dict['estado'])[2:-2]

        
def get_cities(estado):
    slug = slugfy(estado)
    url = f"https://www.guiadoturista.net/america-do-sul/brasil/{slug}/cidades.html"
    
    try:
        
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        todas_li= soup.find_all("li", {"class": "col-12 col-sm-4 col-md-3"})
        enc_print("<br>")
        enc_print(f"------{estado}------<br>")
        enc_print("<br>")



        for li in todas_li:
     
            cidade = li.find('h3').getText()
            enc_print(f"{cidade}<br>") 
    except:
        enc_print("Não Conseguimos localizar as cidades de " + estado) 













get_cities(estado)











