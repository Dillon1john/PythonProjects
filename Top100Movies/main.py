from bs4 import BeautifulSoup
import requests
import lxml

# URL = "https://www.empireonline.com/movies/features/best-movies-2/"
URL = "http://web.archive.org/web/20200518055830/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
html = response.text
soup = BeautifulSoup(html, "html.parser")

# print(soup.prettify())


all_movies = soup.find_all(name="h3", class_="title")
# print(all_movies)
movie_titles = [movie.getText() for movie in all_movies]

# How to reverse list
movies = movie_titles[::-1]


with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
# movies = []
# for movie in all_movies:
#     text = all_movies.getText
#     movies.append(text)


# print(movies)


