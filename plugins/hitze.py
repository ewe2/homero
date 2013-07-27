import simplejson as json
import random
from util import hook
from util import http

@hook.command
def city(inp):
  jsonData = http.get_json('http://www.reddit.com/r/cityporn/.json')
  j= random.choice(jsonData['data']['children'])['data']
  return j['title'] + ' ' + j['url']

@hook.command
def danl(inp, say=None):
  subreddit = [
    "TheRedPill",
    'seduction',
    'CuckoldCommunity',
  ]
  jsonData = http.get_json('http://www.reddit.com/r/' + random.choice(subreddit) + '/.json')
  say('<danl> ' + random.choice(jsonData['data']['children'])['data']['title'].lower())


@hook.regex('oh my god')
def omg(inp, say=None):
    say('oh. my. god.');

@hook.command
def hitze(inp):
    hitzelist = [
      "ahahaaha",
      "lol",
      "heh",
      "omg.",
      "uugh",
      "why..",
      "lol pcgaming",
      "rip",
      "sperg",
      "omg hyle",
    ]

    subreddit = [
    "pics",
    "wtf",
    "cityporn",
    "gaming",
    "minecraftcirclejerk",
    "gifs",
    "nba",

    ]

    noSelf = False
    while noSelf == False:
        jsonData = http.get_json('http://www.reddit.com/r/' + random.choice(subreddit) + '/.json')
        potentialURL = random.choice(jsonData['data']['children'])['data']['url']
        if 'reddit' in potentialURL:
            noSelf = False
        else:
            noSelf = True

    return "<hitz> " + potentialURL + " " + random.choice(hitzelist)

def checkURL(url):
    params = urllib.urlencode({'q':'url:' + url})
    url = "http://www.reddit.com/search.json?%s" % params
    jsan = json.load(urllib2.urlopen(url))
    if len(jsan['data']['children']) > 0:
        return True
    return False


#@hook.event('PRIVMSG')
def hitze_event(paraml, say=None, nick=None):
    if 'hitz' in nick.lower() and 'http://' in paraml[1]:
        if checkURL(paraml[1]):
            say('/!\\ REDDIT ALERT /!\\ REDDIT ALERT /!\\ PLEASE DISREGARD THE PREVIOUS MESSAGE. WE APOLOGISE FOR ANY LIBERTARIANS ENCOUNTERED')
