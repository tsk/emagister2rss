# -*- coding: utf-8 -*-
import web

class index:
    def GET(self):
        return "Nada por aquí"

urls = (
    '/','index'
)

app = web.application(urls, globals())

if __name__ == "__main__":
    import os
    import thread
    import getpass
    import erss
    #look for static/feeds dir
    if os.path.exists("static/feeds") == False:
        os.mkdir("static")
        os.mkdir("static/feeds")
    #Enter email and password to login in grupos.emagister.com
    email = raw_input("Enter your email: ")
    password = getpass.getpass("Password: ")
    thread.start_new_thread(erss.run,(email,password))
    app.run()

