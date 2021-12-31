#Import area
import requests 
import time
import json
import os

class TelegramBot:
    def __init__(self):
        token = '5073775300:AAEFtFZJwNjlYuhEUumIoL_RdGqi6vsMpr4'
        self.url_base = f'https://api.telegram.org/bot{token}/'
    #Start bot
    def Start(self):
        update_id = None
        while True:
            update = self.take_messages(update_id)
            messages = update['result']
            if messages:
                for message in messages:
                    update_id = message['update_id']
                    chat_id = message['message']['from']['id']
                    first_message = message['message']['message_id'] == 1 
                    answer = self.create_answer(message, first_message)
                    self.to_respond(answer, chat_id)
                    
    #Take Messages
    def take_messages(self,update_id):
        link_request = f'{self.url_base}getUpdates?timeout=100'
        if update_id:
            link_request = f'{link_request}&offset={update_id + 1}'
        resultado = requests.get(link_request)
        return json.loads(resultado.content)
    #Create answers
    def create_answer(self,message,first_message):
        message = message['message']['text']
        if first_message == True or message.lower() == 'menu':
         return f'''Hello, Welcome to the online restaurant! Enter the number of the hamburger that you want to order:{os.linesep}1- X-Burger{os.linesep}2- BaconBurger{os.linesep}3- Cheese Bacon Burger'''
        if message == '1':
            return f'''X-Burger - US$ 4,00{os.linesep}Confirm order? (y/n)'''
        if message == '2':
            return f'''BaconBurger - US$ 4,50{os.linesep}Confirm order? (y/n)'''
        if message == '3':
            return f'''Cheese Bacon Burger - US$ 5,00{os.linesep}Confirm order? (y/n)'''

        if message.lower() in ('y', 'yes'):
            return 'Order Confirmed'
        else:
            return 'Do you want to acess the menu? Enter "menu"'   
    
    #To respond
    def to_respond(self,answer,chat_id):
        #To send
        shipping_link = f'{self.url_base}sendMessage?chat_id={chat_id}&text={answer}'
        requests.get(shipping_link)

bot = TelegramBot()
bot.Start()