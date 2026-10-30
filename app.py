from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return redirect(url_for("page1"))

@app.route("/page1")
def page1():
    return render_template("index.html", page="page1")

@app.route("/page2")
def page2():
    return render_template("index.html", page="page2")

@app.route("/page3")
def page3():
    return render_template("index.html", page="page3")

if __name__ == "__main__":
    app.run(debug=True)
