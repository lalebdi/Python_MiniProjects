import web

urls = (
    '/(.*)/(.*)', 'index' # In the first param of the urls, the .* are the parameters for the method GET
)

render = web.template.render("resources/")
app = web.application(urls, globals()) #this is where we instantiate the app


class index: # make sure the name of the class == the second param in the urls (case sensitive)
    def GET(self, name, age):
        return render.main(name, age)


if __name__ == "__main__":
    app.run()



