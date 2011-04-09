import web


class index:
    def GET(self):
        return "Hello, World"

urls = (
    '/','index'
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
