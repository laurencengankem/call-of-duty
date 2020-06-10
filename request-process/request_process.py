from app import app
import threading
from flask_script import Manager
import requests
import time

manager = Manager(app)

@manager.command
def runserver():
    app.run(host ='0.0.0.0', port = 80, debug=True)


def start_service():
    def start_loop():
        not_started = True
        while not_started:
            print('In start loop')
            try:
                r = requests.get('http://127.0.0.1:5001/')
                if r.status_code == 200:
                    print('Server started, quiting start_loop')
                    not_started = False
                print(r.status_code)
            except:
                print('Server not yet started')
            time.sleep(2)

    print('Started runner')
    thread = threading.Thread(target=start_loop)
    thread.daemon = True
    thread.start()

if __name__ == '__main__':
    #start_service()
    manager.run()
