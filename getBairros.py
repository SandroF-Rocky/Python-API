import os
from bs4 import BeautifulSoup
import json
import requests 

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

path = '.'
directory_contents = os.listdir(path)
for estado in directory_contents:    
    path = estado
    
    if estado == "SE" or estado == "SP" or estado == "TO"  :
        cities = os.listdir(path)
        print(cities)
        for city in cities: 
            print()
            print("---")
            print(city)
            print("---")
            print()
            slug = f"{slugfy(city)}-{estado.lower()}"
            url = f"https://www.guiamais.com.br/bairros/{slug}"
            r = requests.get(url)
            soup = BeautifulSoup(r.content, 'html.parser')
            section = soup.find("section", {"class": "cities centerContent"})
            bairros_list = []
            try:
                b = section.find_all("li")
                
                for bairro in b:
                    if len(bairro.getText().strip()) > 1:
                        print(bairro.getText())
                        bairros_list.append(bairro.getText()) 

                    bairros_json = { "bairros": bairros_list }
                    print(bairros_json)

            except:
                print("Error")
                continue
            
            
                
   



























