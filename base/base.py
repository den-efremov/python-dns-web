from flask import Flask, request
import json
from config import Config

class Base:
    app = Flask(__name__.split('.')[0])
    db = None
    @staticmethod
    def asJSON(data):
        if Config.JSONfile is True:
            rv = Base.app.make_response(json.dumps(data, default=Base.encode))
            rv.mimetype = 'application/json'
            return rv
        return json.dumps(data, default=Base.encode)
            
    @staticmethod
    def encode(obj):
        return obj.__dict__
        
class Log:
    @staticmethod
    def debug(*args):
        if len(args) == 2:
            Base.app.logger_name = args[1]
        Base.app.logger.debug(args[0])
        Base.app.logger_name = Base.__name__.split('.')[0]
        
    @staticmethod
    def exception(*args):
        if len(args) == 2:
            Base.app.logger_name = args[1]
        Base.app.logger.exception(args[0])
        Base.app.logger_name = Base.__name__.split('.')[0]
        
class Messages:
    
    def __init__(self):
        self.messages = []
    
    def add(self, msg):
        self.messages.append(msg)
        
    def getAll(self):
        return self.messages