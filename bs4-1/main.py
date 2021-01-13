from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text
# print(response.text)

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)

# story_link = soup.select(selector=".storylink")
# # print(story_link)
#
# for tag in story_link:
#     print(tag.getText())

#  OR
article_tag = soup.find(name="a", class_="storylink")
# print(article_tag.get_text())
article_text = article_tag.get_text()
article_link = article_tag.get("href") # to get the spcicifc value of the tag
article_upvote = soup.find(name="span", class_="score").get_text()
# print(article_text)
# print(article_link)
# print(article_upvote)

# All of the elements
articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [score.getText() for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvotes)