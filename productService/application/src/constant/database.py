
import os

env = os.environ

HOST = env.get("DB_HOST")
PORT = int(env.get("DB_PORT"))
USER = env.get("DB_USER")
PASSWORD = env.get("DB_PASSWORD")
NAME = env.get("DB_NAME")

ERRORS = {
    "FAIL_CONNECTION": "No connection to database"
}