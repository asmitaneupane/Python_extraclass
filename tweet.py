from bs4 import BeautifulSoup
import requests

page = requests.get("https://twitter.com/achiever_priya")
soup = BeautifulSoup(page.content,'html.parser')
all_items = soup.find_all(class_="content")

# for x in range(len(all_items)):
#     content = all_items[x]
#     tweet_text = content.find(class_="js-tweet-text-container")
#     print(x,tweet_text)
for content in(all_items):
    tweet_text = content.find(class_="js-tweet-text-container")
    print(tweet_text)

    # API...