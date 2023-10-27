import requests, os
from send_email import send_email

topic = "cars"

API_KEY = os.getenv("NEWS_API_KEY")
url = f"https://newsapi.org/v2/everything?q={topic}& \
from=2023-09-19&sortBy=publishedAt&apiKey=" + {API_KEY} + "&language=en"

request = requests.get(url)
content = request.json()


email_content = "Subject: Today's News" + "\n"
for article in content['articles']:
    if article['title'] is not None:
        email_content = email_content + "News title: " + article['title'] + '\n' \
        "Visit: " + article['url'] + '\n\n'


email_content = email_content.encode('utf-8')

send_email(message=email_content)

