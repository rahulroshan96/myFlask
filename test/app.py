from flask import Flask, render_template, request, url_for, session, logging


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # return 'hello'
    if request.method == 'POST':
        return request.form
    if request.method =='GET':
        print dir(request.form)
        return 'hello'
    else:
        return request



if __name__ == '__main__':
    print dir(wtforms)
    app.run()