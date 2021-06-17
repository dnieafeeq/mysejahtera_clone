import os
from flask import Flask, flash, request, redirect, url_for, render_template, make_response, abort, session
from werkzeug.utils import secure_filename
from markupsafe import escape

UPLOAD_FOLDER = 'file_uploaded'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = b'\xe4#}\xe0q|\xdc\xc21\xa9\xe6\xe7\x8e!W\xc5'

@app.route("/")
def index():
    return render_template('index.html')
 
@app.route('/about')
def about():
    return '<h1>About Page</h1>'  

@app.route('/home')
def home():
    return render_template('home.html')  

@app.route('/user_esc/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'Username: {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post: {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath: {escape(subpath)}'

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", name=user))
    else:
        return render_template("login.html")

@app.route("/name/<name>")
def user(name):
    return render_template('hello.html', name=name) 

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)    

@app.route('/test')
def test():
   return render_template('test.html')


with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='Muhammad Dinieafiq'))

# with app.test_request_context('/hello', method='POST'):
#     # now you can do something with the request until the
#     # end of the with block, such as basic assertions:
#     assert request.path == '/hello'
#     assert request.method == 'POST'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file', name=filename))
    return render_template('upload.html')


@app.route('/cookies')
def getcookies():
    username = request.cookies.get('username')
    # use cookies.get(key) instead of cookies[key] to not get a
    # KeyError if the cookie is missing.
    return f'Your web cookies: {username}'

@app.route('/setcookies')
def setcookies():
    resp = make_response(render_template('home.html'))
    resp.set_cookie('username', 'the username')
    return resp

@app.route('/index2')
def index2():
    return redirect(url_for('error'))

@app.route('/error/401')
def error():
    abort(401)
    this_is_never_executed()

@app.route('/landingpage')
def landing_page():
    if 'username' in session:
        return f'''Logged in as <h2>{session["username"]}</h2>

            <a href="/logout">Log Out</a>
        '''
    return '''You are not logged in
    <a href="/login2"> Go to Login Session Page </a>
    '''

@app.route('/login2', methods=['GET', 'POST'])
def login2():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('landing_page'))
    return '''
        <h1>Login Session Page</h1>
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('landing_page'))

if __name__ == "__main__":
    app.run(debug=True)