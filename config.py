from flask import Flask
from flaskext.mysql import MySQL


app = Flask(__name__)
app.config['SECRET_KEY'] = '429f3496ac8b1b890375f817cfb99d99' #univer
app.config['TEMPLATES_AUTO_RELOAD'] = True

