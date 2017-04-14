from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
# from flask_script import Manager
from datetime import datetime

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['douban_db']
data = db['data']

app = Flask(__name__)
bootstrap=Bootstrap(app)
moment = Moment(app)

@app.route('/')
def hi():
    return render_template('hi.html',current_time=datetime.utcnow())

@app.route('/douban')
def index():
    result=[]
    for item in data.find():
        result.append(item)
    return  render_template('show.html',data=result)


if __name__ == '__main__':
    app.run()