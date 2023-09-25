from flask import Flask, jsonify, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def home():
    return render_template(
        '/home/home.html',
        title='mavsfocus',
        description='Home page for mavsfocus.com'
    )

@app.route('/roster')
def roster():
    return render_template()

if __name__ == '__main__':
    app.run()