# -*- coding: utf-8 -*-


import requests

class TelegramApi:
    
    def __init__(self):
        self.token = "<Bot-Token>"

    
    def get_message_id(self):
        request = requests.get("https://api.telegram.org/bot{0}/getUpdates".format(self.token))
        content = request.json()
        
        for i_row in content["result"]:
            chat_ids = set()
            chat_ids.add(i_row["message"]["chat"]["id"])
            
        return list(chat_ids)
    
    def send_message(self, text):
        chat_ids = self.get_message_id()
        
        for i_id in chat_ids:
            requests.get("https://api.telegram.org/bot{0}/sendMessage?chat_id={1}&text={2}".format(self.token, i_id, text))