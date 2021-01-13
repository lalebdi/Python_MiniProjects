from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
movies = response.text
# print(movies)

soup = BeautifulSoup(movies, "html.parser")
# print(soup.title)
movie_titles = soup.find_all(name="h3", class_="title")
# print(movie_titles)

movie_list = [movie.getText() for movie in movie_titles]

# for movie in movie_titles:
#     title = movie.getText()
#     movie_list.append(title)

# print(movie_list[::-1])
movies_list = movie_list[::-1]

with open("Movie List.txt", mode="w") as file:
    for movie in movies_list:
        file.write(f"{movie}\n")
