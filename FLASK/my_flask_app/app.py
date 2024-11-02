from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('dresstoimpress.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/sigma')
def sigma():
    return render_template('sigma.html')

@app.route('/secret')
def secret():
    return render_template('secret.html')
     

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)


















    