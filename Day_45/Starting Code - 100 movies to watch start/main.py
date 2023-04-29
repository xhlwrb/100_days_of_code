import requests
from bs4 import BeautifulSoup

# URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
URL = "https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
movie_tags = soup.find_all(name="a", target="_blank", rel="noopener noreferrer")
link_texts = []
movie_names = []
for movie in movie_tags:
    link_texts.append(movie.getText())

for link_text in link_texts:
    if link_text[:24] == "Read Empire's review of ":
        movie_names.append(link_text[24:])

print(movie_names)

with open("movies.txt", "w") as file:
    for order, movie_name in enumerate(movie_names):
        file.write(f"{order+1}) {movie_name}\n")
