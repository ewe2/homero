# THIS PLUGIN IS UNDER CONSTRUCTION
# HA HA HA HA
from util import hook, http
from random import choice

url = 'http://www.textfiles.com/underconstruction/'
src = http.get_html(url)
imgs = src.xpath('//img/@src')
del src

@hook.command(autohelp=False)
def wip(inp):
    '/!\\ UNDER CONSTRUCTION /!\\'
    return url + choice(imgs)
