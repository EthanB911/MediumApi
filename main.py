import requests
import datetime
import xmltodict
import time
from discord_webhook import DiscordWebhook
from bs4 import BeautifulSoup

print("Medium Coinbase post tracker")

def send_To_Webhook(medium_post):
    webhook_url = "https://discord.com/api/webhooks/823903861261598731/zvbKMU2oL7P_KOM24u7ATmPG2vhcsza-8GEubwA5kmPLmrL81DloQILJj5jPjOJl8QnD"
    webhook = DiscordWebhook(url=webhook_url, content=medium_post)
    response = webhook.execute()


def get_posts():
    # headers = {
    #     'Content-Type': "application/x-www-form-urlencoded",
    #     'cache-control': "no-cache",
    #     "Pragma": "no-cache"
    # }
    headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
    request = requests.get("https://medium.com/@coinbaseblog", headers = headers)
    # markup = requests.get("https://ethanbriffa.medium.com/", headers=headers)
    soup = BeautifulSoup(request.content, 'html.parser')
    imgs = soup.find_all("figure", {"class": "paragraph-image"})
    return imgs, request


def get_last_url(images, request):
    if(len(images) != 0):
        first_image = images[0]
        img_url = first_image.find('a').get('href')
        #print(img_url)
        return img_url
    else:
        print("Request failed")
        print(request.headers["Retry-After"])
        time.sleep(int(request.headers["Retry-After"]))
        return False

last_url = 'https://ethanbriffa.medium.com/second-story-957015a76976'
start = time.time()
count = 1
time_now = datetime.datetime.now()
print(time_now.second)
while(time_now.second % 5 != 0):
    time_now = datetime.datetime.now()
    print("Delaying start")

while count < 60:
    # count += 1
    img, req = get_posts()
    last_image = get_last_url(img, req)
    if last_image != False:
        if last_image != last_url:
            print("New Post !! " + last_image)
            send_To_Webhook(last_image)
            last_url = last_image
    time.sleep(8)

end = time.time()
print("elapsed time : ")
print(end - start)

