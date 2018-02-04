from flask import render_template
from flask import request
from teho_package import teho
import TimeBlockAndRecommendation
import json

@teho.route('/')
@teho.route('/index')
def index():
    return render_template('index.html')

@teho.route('/schedule/', methods=['POST'])
def schedule():
    print("hello")
    data = request.get_json(force=True)
    print("hell")
    print(TimeBlockAndRecommendation.schedule(data['param1'], data['param2']))
    return json.dumps(data)
