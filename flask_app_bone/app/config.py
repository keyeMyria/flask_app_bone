#!/usr/bin/env python
# encoding: utf-8


import os

class BaseConfig(object):

	PROJECT = 'zz56'
	PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

	DEBUG = False
	TESTING = False

	# SECRET_KEY =

# class De



if __name__ == '__main__':
	pass