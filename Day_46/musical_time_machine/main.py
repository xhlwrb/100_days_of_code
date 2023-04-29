import requests
from bs4 import BeautifulSoup

# which_year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
# print(which_year)

which_year = "1994-12-30"
url = f"https://www.billboard.com/charts/hot-100/{which_year}"

# connect with the website
response = requests.get(url)
contents = response.text

# soup
soup = BeautifulSoup(contents, "html.parser")
rows = soup.find_all(name="h3", id="title-of-a-story",
                     class_="a-no-trucate")

# get name of songs in a list
name_of_songs = []
for row in rows:
    name_with_spaces = row.getText()
    name = ''.join(c for c in name_with_spaces if c != '\n' and c != '\t')
    name_of_songs.append(name)
print(name_of_songs)

