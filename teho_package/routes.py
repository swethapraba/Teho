from flask import render_template
from teho_package import teho


@teho.route('/')
@teho.route('/index')
def index():
    return render_template('index.html')

@teho.route('/onboard_1')
def onboard_1():
	return render_template('onboard-1.html')

@teho.route('/onboard_2')
def onboard_2():
	return render_template('onboard-2.html')

@teho.route('/onboard_3')
def onboard_3():
	return render_template('onboard-3.html')

@teho.route('/log_before')
def log_before():
	return render_template('log-before.html')

@teho.route('/breathe')
def breathe():
	return render_template('breathe.html')

@teho.route('/log_after')
def log_after():
	return render_template('log-after.html')

@teho.route('/data')
def data():
	return render_template('data.html')
