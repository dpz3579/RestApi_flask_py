from flask import Flask, redirect, jsonify, request
from flask_restful import Api
from route.route import list3

app = Flask(__name__)
api = Api(app)
# app.config['TESTING'] = True
# app.testing = True

# app.run(debug=True, use_debugger=False, use_reloader=True)

for _api in list3:
  api.add_resource(_api.call, _api.api)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=9089)
