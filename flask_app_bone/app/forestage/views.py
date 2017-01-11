from flask import (render_template,
                   redirect, url_for,
                   abort,request,
                   current_app,
                   make_response)
from flask_login import login_required, current_user

from . import forestage





@forestage.route('/', methods=['GET', 'POSTS'])
def v_index():
	print(" ----- ------------- ")

	# return render_template('index.html')
	return render_template('index.html')








