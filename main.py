from flask import Flask, request,render_template

app = Flask(__name__)

@app.route("/")
def matchResume():
    return render_template("matchResume.html")

@app.route("/matcher",methods = ['GET','POST'])
def matcher():


if __name__ == "__main__":
    app.run(debug=True)