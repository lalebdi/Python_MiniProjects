import config
import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = config.STOCK_API_KEY
NEWS_API_KEY = config.NEWS_API_KEY
TWILIO_SID = config.ACCOUNT_SID
TWILIO_AUTH_TOKEN = config.AUTH_TOKEN
VIRTUAL_NUMBER = config.VIRTUAL_NUMBER
PHONE = config.PHONE

# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
# print(response.json())
data = response.json()["Time Series (Daily)"]
# print(data)
data_list = [value for (key, value) in data.items()]
# print(data_list)
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
# print(yesterday_closing_price)


day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
# print(day_before_yesterday_closing_price)


difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
# print(difference)
indicators = None
if difference > 0:
    indicators = "🔺"
else:
    indicators = "🔻"



diff_percent = round((difference / float(yesterday_closing_price)) * 100)
# print(diff_percent)

# change the 0.5 in the if statement below
if abs(diff_percent) >= 0.5:
    # print("Get News")
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    # print(news_response.json())
    articles = news_response.json()["articles"]
    # print(articles)
    three_articles = articles[:3]
    # print(three_articles)
    formatted_articles = [f"{STOCK_NAME}: {indicators}{diff_percent}%\n Headline: {article['title']} \nBrief: {article['description']}" for article in three_articles]
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        print(article)
        message = client.messages.create(
            body=article,
            from_=VIRTUAL_NUMBER,
            to=PHONE
        )

        