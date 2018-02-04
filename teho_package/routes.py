from flask import render_template
from teho_package import teho


@teho.route('/')
@teho.route('/index')
def index():
    return render_template('index.html')

@teho.route('/onboard')
def onboard():
	return render_template('onboard.html')
