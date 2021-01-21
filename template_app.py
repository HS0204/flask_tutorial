from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import redirect

app=Flask(__name__)

database={"lhanseul": "1234", "Lee": "hanseul"}

@app.route('/')
def home_page():
    return render_template("login.html")

# 로그인 페이지

@app.route('/success/<name>/<passwrd>')
def Success(name, passwrd):
    if name in database.keys():
        if passwrd == database[name]:
            return "<h1>Welcome to Website</h1>"
        else:
            return "<h1>Invalid Username of password</h1>"
    else:
        return "<h1>Username doesn't exists</h1>"

    return "<h1>Hello {}</h1>".format(name)

@app.route('/fetch_data', methods=['POST', 'GET'])
def FetchData():
    if request.method == "POST":
        user = request.form['nm']
        password = request.form['pw']
        return redirect(url_for('Success', name=user, passwrd=password))
    else:
        user = request.args.get('nm')
        password = request.args.get('pw')
        return redirect(url_for('Success', name=user, passwrd=password))

# 가입 페이지

@app.route('/signup_page')
def signup_page():
    return render_template("signup.html")

@app.route('/Resigtered/<name>/<passwrd>/<cnfpass>')
def Resigtered(name, passwrd, cnfpass):
    if passwrd == cnfpass:
        database.update({name:passwrd})
        return render_template("signup.html", message="You have successfully signed up")
    else:
        return render_template("signup.html", message="Password didn't matched")

@app.route('/signup', methods=['POST', 'GET'])
def Signup():
    if request.method == "POST":
        user = request.form['snm']
        password = request.form['spw']
        cpassword = request.form['scpw']
        return redirect(url_for('Resigtered', name=user, passwrd=password, cnfpass=cpassword))
    else:
        user = request.args.get('snm')
        password = request.args.get('spw')
        cpassword = request.args.get('scpw')
        return redirect(url_for('Resigtered', name=user, passwrd=password, cnfpass=cpassword))


if __name__ == "__main__":
    app.run(debug=True)