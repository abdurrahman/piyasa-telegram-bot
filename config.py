TOKEN='<your-telegram-token>'
NGROK_URL='https://d782180f9c18.ngrok.io'
HEROKU_APP='https://piyasatr-bot.herokuapp.com'
BASE_TELEGRAM_API_URL='https://api.telegram.org/bot{}'.format(TOKEN)
LOCAL_WEBHOOK_ENDPOINT='{}/webhook'.format(NGROK_URL)
REMOTE_WEBHOOK_ENDPOINT='{}/webhook'.format(HEROKU_APP)

TELEGRAM_INIT_WEBHOOK_URL = '{}/setWebhook?url={}'.format(BASE_TELEGRAM_API_URL, REMOTE_WEBHOOK_ENDPOINT)
TELEGRAM_SEND_MESSAGE_URL = BASE_TELEGRAM_API_URL + '/sendMessage?chat_id={}&text={}'