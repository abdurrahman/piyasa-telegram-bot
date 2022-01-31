TOKEN='1171776040:AAFG99v-MA8KEQCT7tTeG9onihxeLk0xi-8'
NGROK_URL='https://b92a-2001-7d0-84a6-4100-5e9-671b-d59f-70c4.ngrok.io'
HEROKU_APP='https://piyasatr-bot.herokuapp.com'
BASE_TELEGRAM_API_URL='https://api.telegram.org/bot{}'.format(TOKEN)
LOCAL_WEBHOOK_ENDPOINT='{}/webhook'.format(NGROK_URL)
REMOTE_WEBHOOK_ENDPOINT='{}/webhook'.format(HEROKU_APP)

TELEGRAM_INIT_WEBHOOK_URL = '{}/setWebhook?url={}'.format(BASE_TELEGRAM_API_URL, LOCAL_WEBHOOK_ENDPOINT)
TELEGRAM_SEND_MESSAGE_URL = BASE_TELEGRAM_API_URL + '/sendMessage?chat_id={}&text={}'