from bs4 import BeautifulSoup
import requests
import lxml

url = input("Введите путь к файлу с сайта ranobe.me\n")
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

path = input("введите путь к точке сохранения\n")

title = soup.find("h2").text
chapter = soup.find("div", class_="chapter").text

with open(path + title + ".txt", "w+", encoding="utf-8") as file:
    file.write(chapter)
