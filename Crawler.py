# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


class PriceCrawler:
    
    def craw(self, url): 
        
        return self.get_response(url)
    
    def get_response(self, url):
        request = requests.get(url)
        html = request.text
        
        return self.data_mine(html)
    
    def data_mine(self, html):
        
        soup = BeautifulSoup(html, 'html.parser')
        
        """ 
        This is an example of what you need to do to web-scraping the page.
        
        product_title          = soup.select('h1.title')[0].text
        product_old_price      = soup.select('div.old_price-cm')[0].text
        product_discount_price = soup.select('div.discount_price')[0].text
        product_ticket_price   = soup.select('span.ticket_price')[0].text
        
        Dictionary with the web-scrapping results.
        
        values = {
                  'product_name':           product_title, 
                  'product_old_price':      product_old_price, 
                  'product_discount_price': product_discount_price, 
                  'product_ticket_price':   product_ticket_price
                  }
       """
        return values 