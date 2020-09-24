
from flask import Flask
from eurekaClientShare.client.client import DiscoveryClient
from constant.discover import INFO_DISCOVER
from configuration.database import Database


db = Database()
discover = DiscoveryClient(INFO_DISCOVER)

app = Flask(__name__)
