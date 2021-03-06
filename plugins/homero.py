# alligator
import random
import requests
from util import hook, http

#search_url = "https://gdata.youtube.com/feeds/api/videos?v=2&alt=jsonc&category=los%2Csimpsons&max-results=1&start-index="
yt_url = "http://youtu.be/%s/"

def searchURL(cat):
    return "https://gdata.youtube.com/feeds/api/videos?v=2&alt=jsonc&category=" + cat.replace(' ','%2C') + "&max-results=1&start-index=" + str(random.randint(1,20))

@hook.command(autohelp=False)
def homero(inp):
    '.homero <query> -- los simpsons?'
    return requests.get('http://simpsons-latino.tumblr.com/random').url

@hook.command
def kula(inp):
    j = http.get_json(searchURL("kula world"))
    if j['data']['totalItems'] == 0:
        return 'no results found'

    title = j['data']['items'][0]['title']
    vid = j['data']['items'][0]['id']
    return title + ' - ' + yt_url % vid
    

@hook.command
def sylauxe(inp):
    sylauxeList = [
        "diaper",
        "anime",
        "my little sister cant be this cute",
        "pony",
        "anime obama"
        ]
    j = http.get_json(searchURL(random.choice(sylauxeList)))

    if j['data']['totalItems'] == 0:
        return 'no results found'

    title = j['data']['items'][0]['title']
    vid = j['data']['items'][0]['id']
    return title + ' - ' + yt_url % vid
