import requests
from bs4 import BeautifulSoup
import colorama
from colorama import Fore

# A bridge between python and the website we are collecting data from
data = requests.get("https://www.worldometers.info/coronavirus/")
# Enables us to access the html of the website
soup = BeautifulSoup(data.text, "html.parser")
body = soup.find("body")
table = body.find("table", {"id": "main_table_countries_today"})
tbody = table.find("tbody")

# Dataset along the 15 columns
parameters =[ Fore.GREEN+"","Total cases :", "New cases :", "Total deaths :", "New deaths :", "Total recovered :",
              "New recovered :","Active cases :", "Critical cases :", "Total cases / mil :", "Deaths / mil :",
              "Total tests :", "Tests / mil : ", "Population : "]
columns = 15
get = []
def func(x):
    for tr in tbody.findAll(x):
        for i in range(0, columns - 1):
            if (i == 1):
                get.append("--------------------\n")
            x = tr.findAll("td")[i + 1].text.strip()
            para = parameters[i]
            get.append(para + x)
        get.append("\n--------------------")

# y = countries and z = continents
y = "tr", {"style": ["", "background-color:#F0F0F0", "background-color:#EAF7D5"]}
z = "tr", {"class" : ["total_row_world"]}
func(y), func(z)

for i in range(0, len(get)):
    print(get[i])
