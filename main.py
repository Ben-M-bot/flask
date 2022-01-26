from flask import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/success/<name>')
def success(name):
    return "hello %s" % name

@app.route('/login_page')
def login_page():
    return render_template("login.html")

@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["name"]
        return redirect(url_for("success", name=user))
    else:     #Not really needed as POST is being used
        user = request.args.get("name")
        passw = request.args.get("password")
        return redirect((url_for("success", name=user)))

@app.route('/sign_up_page')
def sign_up_page():
    return render_template("signup.html")

@app.route('/sign_up', methods=["POST", "GET"])
def sign_up():
    if request.method == "POST":
        usern = request.form["name"]
        passw = request.form["password"]
        return redirect(url_for("success", name=usern))
    else:     #Not really needed as POST is being used
        usern = request.args.get("name")
        password = request.args.get("password")
        return redirect(url_for("success", name=usern))

if __name__ == '__main__':
    app.run(debug=True)
