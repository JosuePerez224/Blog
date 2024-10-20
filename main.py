from MyBlog import app#<-- Import the app from __init__

#This is the first page that is going to be rendered
@app.route("/")
def index():
    return "<h1> Hola mundito </hi>"

#Initialization of the app
if __name__ == "__main__":
    app.run(port="4000", debug=True)