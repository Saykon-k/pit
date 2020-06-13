import requests
from bs4 import BeautifulSoup
import numpy as np
vgm_url = 'http://www.rating.unecon.ru'
html_text = requests.get(vgm_url).text
soup = BeautifulSoup(html_text, 'html.parser')
data_students_kurse = {}
for a in soup.find_all('a', href=True):
    data_students_kurse[a.get_text()] = 'http://www.rating.unecon.ru/'+a.get('href')
print(data_students_kurse)