from notifier import notify, Notifier
import os

TG_ID = os.environ['TG_ID']
TG_TOKEN = os.environ['TG_TOKEN']
WEBHOOK_URL = os.environ['WEBHOOK_URL']

notifier = Notifier(api_token=TG_TOKEN, chat_id=TG_ID, webhook_url=WEBHOOK_URL)
notifier(msg='Test', title='Manual call')
