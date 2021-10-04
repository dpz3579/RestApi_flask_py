from flask import Flask
app = Flask(__name__)

from bl.bl import init, welcome, hello, print_list, tea, test

# Please use unique / different function names for each and every API else it will give assertion value
apinames = [
  { 'nm': '', 'func': init },
  { 'nm': 'hello', 'func': welcome },
  { 'nm': 'person', 'func': hello },
  { 'nm': 'numbers', 'func': print_list },
  { 'nm': 'teapot', 'func': tea },
]

class APIClass(object):
  def __init__(self, name, function):
    self.api = '/' + name + '/'
    self.defnm = name + '()'
    self.call = function

basicapi = []

for _api in apinames:
  # print(api, api['nm'])
  basicapi.append(APIClass(_api['nm'], _api['func']))
