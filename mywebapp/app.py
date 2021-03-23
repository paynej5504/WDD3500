from flask import Flask, url_for, redirect
app = Flask(__name__)

# route to localhost:5000
@app.route('/')
def hello_world():
# "Hello World" will show in the screen
 return "Hello World"

# admin route
@app.route('/admin')
def admin_page():
# message displayed on page
 return "Welcome to the admin page"

# guest route
@app.route('/guest/<guest>')
def hello_guest(guest):
# message displayed on page
    return 'Hello %s as Guest' % guest

# user route
@app.route('/user/<name>')
def user_sort(name):
# if <name> is equal to 'admin' the user will be redirected to the admin page
    if name == 'admin':
        return redirect(url_for('admin_page'))
# if the user is not an admin they will be redirected to the guest page
    else:
        return redirect (url_for('hello_guest', guest = name))


if __name__ == '__main__':
 app.run()