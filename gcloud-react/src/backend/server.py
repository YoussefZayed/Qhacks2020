#!usr/bin/python3.8
from flask import Flask, request, jsonify, after_this_request
from spiralModel import testSpiral
import base64

app = Flask(__name__)

@app.route('/spiral_test/', methods=['POST'])
def spiral():
   @after_this_request
   def add_header(response):
      response.headers.add('Access-Control-Allow-Origin', '*')
      return response

   image = request.form['image']
   print(image)
   with open("imageToSave.svg", "wb") as fh:
      fh.write(base64.standard_b64decode(image))
      result = testSpiral('imageToSave.svg')
      print(result)
      return result


   

if __name__ == '__main__':
   app.run()