from teho_package import teho

@teho.route('/')
@teho.route('/index')
def index():
    return 'hello world!'
