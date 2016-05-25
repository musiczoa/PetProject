from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/goto_login')
def goto_login():
    return render_template('goto_login.html')


@app.route('/login', methods=['POST'])
def login():
    id = request.form['id']
    pw = request.form['pw']
    if id == 'admin' and pw == 'svm1202':
        return render_template('login_success.html')
    else:
        return render_template('login_fail.html')


@app.route('/logout')
def logout():
    return render_template('goto_login.html')

if __name__ == '__main__':
    app.run()
