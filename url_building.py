from flask import Flask, redirect, url_for

app=Flask(__name__)


@app.route('/admin')
def message_admin():
    return "<h1>Hello Admin</h1>"

@app.route('/user/<name>')
def message_user(name):
    return "<h1>Hello {}</h1>".format(name)

@app.route('/user/<name_admin>')
def message_user_admin(name_admin):
    if name_admin == "admin":
        return redirect(url_for(message_admin))
    else:
        return redirect(url_for(message_user, name=name_admin))

if __name__ == "__main__":
    app.run(debug=True)