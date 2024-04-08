from flask import Flask`x`

app = Flask(__name__)

@app.route('/login')
def login():
    return 'Login endpoint'

@app.route('/home')
def home():
    return 'Home endpoint'

if __name__ == '__main__':
    app.run(debug=True,port=5000, host='0.0.0.0')
