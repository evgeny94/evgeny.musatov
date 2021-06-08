from flask import Blueprint, render_template, redirect, url_for

# homepage blueprint definition
assignment10 = Blueprint('assignment10', __name__, static_folder='static', static_url_path='/assignment10', template_folder='templates')


# Routes
@assignment10.route('/assignment10', methods=['GET', 'POST', 'DELETE', 'UPDATE'])
def index():
    return render_template('assignment10.html')

