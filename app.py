from flask import Flask, render_template , request
app = Flask(__name__)
@app.route('/index')
def main():
    return render_template('index.html')

@app.route('/login')
def showLogin():
    return render_template('login.html')

@app.route('/signup')
def showSignUp():
    return render_template('signup.html')


if __name__ == '__main__':
  app.run(debug=True)
