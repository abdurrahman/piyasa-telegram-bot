TOKEN='1097144437:AAGmrLEQsZketiSzzRzHUrbAvBb9pxuryV8'
NGROK_URL='https://06ca68a6f943.ngrok.io'
HEROKU_APP='https://goldtelegrambot.herokuapp.com'
BASE_TELEGRAM_API_URL='https://api.telegram.org/bot{}'.format(TOKEN)
LOCAL_WEBHOOK_ENDPOINT='{}/webhook'.format(NGROK_URL)
REMOTE_WEBHOOK_ENDPOINT='{}/webhook'.format(HEROKU_APP)

TELEGRAM_INIT_WEBHOOK_URL = '{}/setWebhook?url={}'.format(BASE_TELEGRAM_API_URL, REMOTE_WEBHOOK_ENDPOINT)
TELEGRAM_SEND_MESSAGE_URL = BASE_TELEGRAM_API_URL + '/sendMessage?chat_id={}&text={}'