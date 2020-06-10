import requests
from bs4 import BeautifulSoup
import numpy as np
vgm_url = 'http://www.rating.unecon.ru/index.php?&y=2018&k=1&f=1&up=12020&g=all&upp=all&sort=fio&ball=hide&s=4'
html_text = requests.get(vgm_url).text
soup = BeautifulSoup(html_text, 'html.parser')
kol_subject = -1
bol = False
name_subject = []
for link in soup.find_all('th'):
        if "∑баллов" == link.get_text() or bol :
            bol = True
            kol_subject+=1
for link in soup.find_all('th'):
    name_subject.append(link.get_text())
name_subject = name_subject[5::]
name_subject.insert(0,"номер")
name_subject.insert(1,"ФИО")
name_subject.insert(2,"№ группы")

kol_subject+=3
kol_subject*=2
students = []
for link in soup.find_all('tbody'):
    for link2 in link.find_all('td'):
        prom = link2.get_text()
        if prom == "":
            prom = "0"
        students.append(prom)
students = np.array(students)
all_students = np.split(students,kol_subject)
print(name_subject)
print(all_students)