from bs4 import BeautifulSoup
import requests

# import lxml
#
# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # soup = BeautifulSoup(contents, "lxml")
# print(soup.title)
# print(soup.title.string)
# print(soup)
# print(soup.prettify())
#
# print(soup.a)
# print(soup.p)
#
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# name = soup.select_one(selector="#name")
# print(name)
#
# headings = soup.select(".heading")
# print(headings)

response = requests.get("https://news.ycombinator.com/")

response.text()

