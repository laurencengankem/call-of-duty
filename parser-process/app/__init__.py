from flask import Flask
import threading

app = Flask(__name__)

from app import route


