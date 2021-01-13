from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
movies = response.text
# print(movies)

soup = BeautifulSoup(movies, "html.parser")
# print(soup.title)
movie_titles = soup.find_all(name="h3", class_="title")
# print(movie_titles)

movie_list = []

for movie in movie_titles:
    title = movie.getText()
    movie_list.append(title)

print(movie_list)
