from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/blank")
def blank():
    return render_template("blank.html")

@app.route("/button")
def button():
    return render_template("button.html")

@app.route("/chart")
def chart():
    return render_template("chart.html")

@app.route("/element")
def element():
    return render_template("element.html")

@app.route("/error")
def error():
    return render_template("error.html")

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/signin")
def signin():
    return render_template("signin.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/table")
def table():
    return render_template("table.html")

@app.route("/typography")
def typography():
    return render_template("typography.html")

@app.route("/widget")
def widget():
    return render_template("widget.html")

if __name__=="__main__":
    app.run(debug=True)