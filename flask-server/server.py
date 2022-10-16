from sys import api_version
from flask import Flask, render_template, request, redirect, url_for, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import random
import qrcode
import PIL
from PIL import Image
import requests

db = SQLAlchemy()

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    


app = Flask(__name__)


@app.route('/test-post', methods = ['POST'])
def test_post():
    todo_data = request.get_json()
    print(todo_data)
    try:
        print(todo_data['name']+ str(todo_data['age']))
        generateQrcode(todo_data['name']+ str(todo_data['age']))
    except:
        print("dictionary error")
    return 'hello world i hate programming', 200

@app.route("/get-image")
def get_image():
    
    return send_file("./good.png")

@app.route("/image-download")
def image_downlaod():
    return render_template("image-download.html")

# this method generates a qr code and saves it on the server
def generateQrcode(x = "placeholder"):
    img = qrcode.make(str(x))
    img.save("good.png")
    
    
if __name__ == '__main__':
    print("Your server is running!")
    app.run(debug=True)