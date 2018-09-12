import matplotlib.pyplot as plt
from bs4 import BeautifulSoup as bs
import requests

year = []
person = []
url = "http://www.daxi-hro.tycg.gov.tw/home.jsp?id=24&parentpath=0,21,22"
content = requests.get(url).text
parse = bs(content, "html.parser")
data1 = parse.find("tbody")
rows = data1.find_all("tr")
for row in rows:
    cols = row.find_all("td")
    if(len(cols) > 0):
        year.append(cols[0].text[:-1])
        person.append(cols[1].text)
        
plt.plot(year, person, linewidth="2.0")
plt.title("桃園市大溪區歷年戶數")
plt.xlabel("年度")
plt.ylabel("戶數")
plt.show()
