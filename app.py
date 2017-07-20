from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main/home.html')

@app.route('/about')
def about():
    return render_template('main/about.html')

@app.route('/contact')
def contact():
    return render_template('main/contact.html')

@app.route('/signup')
def signup():
    return render_template('user/signup.html')

@app.route('/login')
def login():
    return render_template('user/login.html')

@app.route('/<string:name>', methods=['GET','POST'])
def test(name):
    return name

@app.route('/forgot')
def forgot():
    return render_template('user/forgot.html')

if __name__ == '__main__':
    app.run()