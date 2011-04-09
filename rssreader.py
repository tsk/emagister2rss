
import re
import urllib
import urllib2
import cookielib
import emagister2rss

def EtoRss(email, password):
    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    data = urllib.urlencode({"mail":email,"password":password})
    url_s = "http://grupos.emagister.com/index/signin"

    opener.open(url_s,data)

    url = "http://grupos.emagister.com"
    urls = {'wall':url+"/userhome/#wall_all",
            'groups':url+"/perfil/grupos",}

    for url_ in urls:
        s = opener.open(urls[url_])
        getattr(emagister2rss,'rss_'+url_)(s.read(),opener)

if __name__ == "__main__":
    import time
    import getpass
    import os
    if os.path.exists("static/feeds") == False:
        os.mkdir("static")
        os.mkdir("static/feeds")
    email = raw_input("Enter your email: ")
    password = getpass.getpass("Password: ")
    while(1):
        EtoRss(email,password)
        time.sleep(60)
