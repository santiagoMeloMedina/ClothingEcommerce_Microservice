
import sys
import signal
from configuration.app import app, discover, db
import configuration.database as db
from multiprocessing import Process

def handler(signal, frame):
    print("Turning off dicovery client..")
    discover.stop()
    print("Turning off database..")
    db.release()
    print("Turning off flask server..")
    server = Process(target=app.run)
    server.start()
    server.terminate()
    server.join()
    sys.exit(0)

signal.signal(signal.SIGINT, handler)
