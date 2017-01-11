
from flask import render_template


from . import admin

@admin.route('/')
def v_index():
	# return render_template('admin/index.html')
	return render_template('index.html')