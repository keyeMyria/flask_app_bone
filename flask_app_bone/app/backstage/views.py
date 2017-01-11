
from flask import render_template

from . import backstage


@backstage.route('/')
def v_index():
	print(" -====== ")
	return render_template('index.html')



