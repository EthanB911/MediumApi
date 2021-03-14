import requests
import datetime
import xmltodict


print("Medium Coinbase post tracker")

def get_posts():
    response = requests.get("https://medium.com/feed/@coinbaseblog")
    my_dict = xmltodict.parse(response.text)
    return my_dict['rss']['channel']['item']

def get_last_date(last_post):
    last_date = str(last_post['pubDate'])
    size = len(last_date)
    date = last_date[:size - 4]
    return datetime.datetime.strptime(date, '%a, %d %b %Y %H:%M:%S')

all_posts = get_posts()
last_post_date = get_last_date(all_posts[0])

#compare with current
current_date = datetime.datetime.now()


