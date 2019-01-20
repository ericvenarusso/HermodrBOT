# -*- coding: utf-8 -*-

from Telegram import TelegramApi
from Crawler  import PriceCrawler


class Hermodr:
    
    def __init__(self):
        self.url = "<e-commerce product link>"
        self.values = PriceCrawler().craw(self.url)
        
    def execute(self):
        text = "<Your custom message>"
        TelegramApi().send_message(text)
     
        
Hermodr().execute()