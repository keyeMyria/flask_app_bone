from flask import jsonify, request, url_for

from . import api_1_0


@api_1_0.route('/orders/')
def get_orders():
	print(" =============== 00000000000 ")
	return jsonify({
		'payload':[],
		'code':0,
		'total':0,
		'msg':'some message'
	});

@api_1_0.route('/order/<string:order_id>')
def get_order(order_id):
	print(" =====--=-=-=-= 333333333333 ")
	return jsonify({
		'code':0,
		'payload':{},
		'msg':"some message11"
	})