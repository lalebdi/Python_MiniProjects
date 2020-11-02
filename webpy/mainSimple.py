import web

urls = (
    '/(.*)', 'index'
)

app = web.application(urls, globals()) #this is where we instantiate the app


class index:
    def GET(self, name):
        # print("Hello", name, "How are you?")
        return "<h1> Hello " + name + ". </h1> How are you?"


if __name__ == "__main__":
    app.run()