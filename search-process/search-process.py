from app import app
import threading
from flask_script import Manager
import requests
import time



manager = Manager(app)


@manager.command
def runserver():
    app.run(host ='0.0.0.0', port =80, debug=True)


if __name__ == '__main__':
    manager.run()
