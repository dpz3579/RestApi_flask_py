from flask_restful import Resource

class init(Resource):
  def get(self):
    return "Init home page!", 200

class welcome(Resource):
  def get(self):
    return "Hello World!", 200

class hello(Resource):
  def get(self):
    return {'name':'Jimit', 'address':'India'}

class print_list(Resource):
  def get(self):
    return list(range(5))

class tea(Resource):
  def get(self):
    return {'name':'Jimit', 'address':'India'}
  # return "Would you like some tea?", 418

class test(Resource):
  def get(self):
    data = {'name': 'john smith'}
    return data, 418
