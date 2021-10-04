from flask import Flask, redirect, jsonify, request
from flask_restful import Api
# from flask_session import Session
from route.route import basicapi
# from pymongo import MongoClient

# client = MongoClient('mongodb://localhost:27017/')

app = Flask(__name__)
# SESSION_COOKIE_NAME = 'pysess'
# # SESSION_COOKIE_DOMAIN = '*.xyz.io'
# # SESSION_COOKIE_PATH
# PERMANENT_SESSION_LIFETIME = (30 * (365 * 24 * 60 * 60))  # 30 years
# SESSION_TYPE = 'mongodb'

# SESSION_USE_SIGNER = True
# SESSION_KEY_PREFIX = "izafa"
# SESSION_MONGODB = client # db instance
# SESSION_MONGODB_DB = "sessions"
# SESSION_MONGODB_COLLECT = "app_sessions"

app.config.from_object(__name__)
# Session(app)

api = Api(app)
# # app.config['TESTING'] = True
# # app.testing = True

# app.run(debug=True, use_debugger=False, use_reloader=True)

for _api in basicapi:
  api.add_resource(_api.call, _api.api)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=9989)
