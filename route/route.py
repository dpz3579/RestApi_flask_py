from flask import Flask
app = Flask(__name__)

from bl.bl import welcome, hello, print_list, tea, test

apinames = [
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

list3 = []

for api in apinames:
  # print(api, api['nm'])
  list3.append(APIClass(api['nm'], api['func']))
