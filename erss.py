# -*- coding: utf-8 -*-
import urllib
import urllib2
import cookielib
import emagister2rss

def login(email, password):
    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    data = urllib.urlencode({"mail":email,"password":password})
    url_s = "http://grupos.emagister.com/index/signin"

    opener.open(url_s,data)
    
    return opener

def EtoRss(opener):
    url = "http://grupos.emagister.com"
    urls = {'wall':url+"/userhome/#wall_all",
            'groups':url+"/perfil/grupos",}

    for url_ in urls:
        s = opener.open(urls[url_])
        content = (s.read()).decode("latin-1")
        getattr(emagister2rss,'rss_'+url_)(content,opener)

def run(email,password):
    import time
    opener = login(email,password)
    while(1):
        EtoRss(opener)
        time.sleep(60)
