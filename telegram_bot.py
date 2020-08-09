import requests
import codecs
import json

from config import TELEGRAM_SEND_MESSAGE_URL

class TelegramBot:

    def __init__(self):
        """"
        Initializes an instance of the TelegramBot class.

        Attributes:
            chat_id:str: Chat ID of Telegram chat, used to identify which conversation outgoing messages should be send to.
            text:str: Text of Telegram chat
            first_name:str: First name of the user who sent the message
            last_name:str: Last name of the user who sent the message
        """

        self.chat_id = None
        self.text = None
        self.first_name = None
        self.last_name = None


    def parse_webhook_data(self, data):
        """
        Parses Telegram JSON request from webhook and sets fields for conditional actions

        Args:
            data:str: JSON string of data
        """

        message = data['message']

        self.chat_id = message['chat']['id']
        self.incoming_message_text = message['text'].lower()
        self.first_name = message['from']['first_name']
        self.last_name = message['from']['last_name']


    def action(self):
        """
        Conditional actions based on set webhook data.

        Returns:
            bool: True if the action was completed successfully else false
        """

        success = None

        if self.incoming_message_text == '/hello':
            self.outgoing_message_text = "Hello {} {}!".format(self.first_name, self.last_name)
            success = self.send_message()

        if self.incoming_message_text == '/altin':
            self.outgoing_message_text = self.parse_gold_prices_from_service()
            success = self.send_message()

        if self.incoming_message_text == '/doviz':
            self.outgoing_message_text = self.parse_currency_prices_from_service()
            success = self.send_message()
        
        return success


    def send_message(self):
        """
        Sends message to Telegram servers.
        """

        res = requests.get(TELEGRAM_SEND_MESSAGE_URL.format(self.chat_id, self.outgoing_message_text))

        return res.status_code == 200

    def parse_gold_prices_from_service(self):
        """
        Retrieves local gold price data
        """
        res = requests.get('http://www.kulcealtin.com/altinjson/')
        decoded_data = json.loads(res.text.encode().decode('utf-8-sig')) # res.text.encode().decode('utf-8-sig')
        result = f"""Gram Altın: {decoded_data['GAAl']} Alış | {decoded_data['GASat']} Satış
Çeyrek Altın: {decoded_data['CAl']} Alış | {decoded_data['CSat']} Satış
Yarım Altın: {decoded_data['YAl']} Alış | {decoded_data['YSat']} Satış
Tam Altın: {decoded_data['TAl']} Alış | {decoded_data['TSat']} Satış
Külçe Altın: {decoded_data['GUAl']} Alış | {decoded_data['GUSat']} Satış"""
        return result
         
    def parse_currency_prices_from_service(self):
        """
        Retrieves local currencies
        """
        res = requests.get('http://www.kulcealtin.com/tcmbjson/')
        decoded_data = json.loads(res.text.encode().decode('utf-8-sig'))
        result = f"""🇺🇸 : {decoded_data['usdAl']} Alış | {decoded_data['usdSat']} Satış
🇪🇺 : {decoded_data['eurAl']} Alış | {decoded_data['eurSat']} Satış
🇬🇧 : {decoded_data['gbpAl']} Alış | {decoded_data['gbpSat']} Satış
🇨🇭 : {decoded_data['chfAl']} Alış | {decoded_data['chfSat']} Satış
🇯🇵 : {decoded_data['jpyAl']} Alış | {decoded_data['jpySat']} Satış"""
        return result

    @staticmethod
    def init_webhook(url):
        """
        Initializes the webhook

        Args:
            url:str: Provides the telegram server with a endpoint for webhook data
        """

        requests.get(url)


