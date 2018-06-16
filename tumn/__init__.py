from flask import Flask

app = Flask(__name__)

__import__('tumn.resources')
