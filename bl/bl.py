from flask import jsonify
from flask_restful import Resource

class welcome(Resource):
  def get(self):
    return "Hello World!"

class hello(Resource):
  def get(self):
    return jsonify({'name':'Jimit', 'address':'India'})

class print_list(Resource):
  def get(self):
    return jsonify(list(range(5)))

class tea(Resource):
  def get(self):
    return jsonify({'name':'Jimit', 'address':'India'}), 200
  # return "Would you like some tea?", 418

class test(Resource):
  def get(self):
    return jsonify({'name':'test', 'address':'India'}), 200
