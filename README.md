# Notifier Function Status
This library uses a decorator to show a toast in your screen or send you a email, message to discord channel or use a Telegram bot to send you a message when your function has finished.

## Requeriments

Please install this packages by yourself depending on your OS:

- Windows: ```pip3 install win10toast```
- Ubuntu: ```apt-get install libnotify-bin``` (if don't work try searching how install notify-send for your distro of Linux)

## Usage

All that you need to do is use a decorator and some specific parameters, like in the following example:

```python
from notifier import notify

@notify(email='enmanuelmag@cardor.dev')
def your_function():
    print('Hello World!')
```

### Parameters

- **title**: the title of toast notification, by defult is: `Function finished`.
- **email**: the email of user, by defult is: `None`.
- **api_token**: the api token of your Telegram bot, by defult is: `None`. You could use [BotFather](https://t.me/botfather) to create a personal bot.
- **chat_id**: the chat id to send the message, by defult is: `None`. If you account is public you could use your username (@username), otherwise you could use the chat id, you'll find [here](https://t.me/username_to_id_bot).
- **webhook_url**: the url of webhook to send message to discord channel, by defult is: `None`.
- **msg**: the message of toast notification, by default is: `Your function has finished`.
- **duration**: the time, in seconds, that the nottications will show, by default is `8`.
- **urgency**: the urgency of the notifcation. By defualt is `normal`. The options are:
  - low.
  - normal.
  - critical.

Made with ❤️ by [Enmanuel Magallanes](https://cardor.dev)
