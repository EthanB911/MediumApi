import requests
import datetime
import xmltodict
import time
from bs4 import BeautifulSoup

print("Medium Coinbase post tracker")

def get_posts():
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        "Pragma": "no-cache"
    }
    request = requests.get("https://medium.com/@coinbaseblog", headers=headers)
    # markup = requests.get("https://ethanbriffa.medium.com/", headers=headers)
    soup = BeautifulSoup(request.content, 'html.parser')
    imgs = soup.find_all("figure", {"class": "paragraph-image"})
    return imgs, request


def get_last_url(images, request):
    if(len(images) != 0):
        first_image = images[0]
        img_url = first_image.find('a').get('href')
        print(img_url)
        return img_url
    else:
        print("Request failed")
        print(request.headers["Retry-After"])
        time.sleep(int(request.headers["Retry-After"]))
        return False

last_url = 'https://ethanbriffa.medium.com/second-story-957015a76976'

count = 1
while count < 53:
    count += 1
    img, req = get_posts()
    last_image = get_last_url(img, req)
    if last_image != False:
        if last_image != last_url:
            print("New Post !! " + last_image)
            last_url = last_image
    time.sleep(10)



