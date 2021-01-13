from bs4 import BeautifulSoup


with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser') # if the HTML parser is not working consider using the lxml (import it)
# print(soup.title)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.a)
# print(soup.li)
# print(soup.p)

