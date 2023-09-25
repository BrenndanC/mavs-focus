from flask import Flask, jsonify, render_template, json
from scripts.get import team_data_dict
import scripts.config

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def home():
    data = json.dumps(team_data_dict())
    return render_template(
        '/home/home.html',
        title='mavsfocus',
        description='Home page for mavsfocus.com',
        team_data = data
    )

@app.route('/roster')
def roster():
    return render_template()

if __name__ == '__main__':
    app.run()