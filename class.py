from flask import Flask

app = Flask(__name__)

for i in dir(app):
	print(i)

for i in dir(app.config):
	print(i)