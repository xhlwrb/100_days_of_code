import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


def telegram_bot_sendtext(bot_message):
    bot_token = "6093731261:AAH_sXfvkElXekEfEfttw-w7h3rp93Rw1t4"
    bot_chatID = "5738351415"
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=HTML&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
alpha_vantage_endpoint = "https://www.alphavantage.co/query"
alpha_vantage_api_key = "V2FFEI53PN282QCD"

alpha_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": alpha_vantage_api_key,
}

response = requests.get(alpha_vantage_endpoint, params=alpha_params)
response.raise_for_status()
alpha_vantage_data = response.json()

iter_alpha = iter(alpha_vantage_data["Time Series (Daily)"])
yesterday = next(iter_alpha)
the_day_before_yesterday = next(iter_alpha)
yesterday_price = float(alpha_vantage_data["Time Series (Daily)"][yesterday]["4. close"])
the_day_before_price = float(alpha_vantage_data["Time Series (Daily)"][the_day_before_yesterday]["4. close"])


# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
news_endpoint = "https://newsapi.org/v2/everything"
news_api_key = "b57ab19df0eb482d91049771fa5d0247"

news_params = {
    "q": COMPANY_NAME,
    "apiKey": news_api_key,
}

response = requests.get(news_endpoint, params=news_params)
response.raise_for_status()
news_data = response.json()

iter_news = iter(news_data["articles"])
news1 = next(iter_news)
news2 = next(iter_news)
news3 = next(iter_news)

# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
divide = yesterday_price / the_day_before_price
# print(' '.join(news3["description"].split(" ")[5:]))
if divide >= 1.04:
    to_send = f"{STOCK}: 🔺{round((divide-1) * 100)}%\nHeadline: {news1['title']}\nBrief: {news1['description']}"
    telegram_bot_sendtext(to_send)
    to_send = f"{STOCK}: 🔺{round((divide-1) * 100)}%\nHeadline: {news2['title']}\nBrief: {news2['description']}"
    telegram_bot_sendtext(to_send)
    to_send = f"{STOCK}: 🔺{round((divide-1) * 100)}%\nHeadline: {news3['title']}\nBrief: {news3['description']}"
    telegram_bot_sendtext(to_send)
elif divide <= 0.95:
    to_send = f"{STOCK}: 🔻{round((1-divide) * 100)}%\nHeadline: {news1['title']}\nBrief: {news1['description']}"
    telegram_bot_sendtext(to_send)
    to_send = f"{STOCK}: 🔻{round((1-divide) * 100)}%\nHeadline: {news2['title']}\nBrief: {news2['description']}"
    telegram_bot_sendtext(to_send)
    to_send = f"{STOCK}: 🔻{round((1-divide) * 100)}%\nHeadline: {news3['title']}\nBrief: {news3['description']}"
    telegram_bot_sendtext(to_send)


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

