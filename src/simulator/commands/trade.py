import logging
import requests
from src.simulator.commands.command import Command


class Trade(Command):
    """Trade Command"""
    
    def rest_request(self):
        url = ""
        data = {}
        
        response = requests.post(url, json=data)
        logging.debug(f"Cancel Order Response: {response.status_code}")
    
    
    def execute(self):
        pass