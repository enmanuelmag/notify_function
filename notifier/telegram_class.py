import requests

class Telegram(object):
  def __init__(self, api_token, chat_id) -> None:
    self.__api_token = api_token
    self.__chat_id = chat_id
  
  def send_message(self, title='', description='', error=None, start=None, end=None):
    if error is None:
      message = f'*{title}*  🚀\n'
    else:
      message = f'*{title}*  💥\n'
    if description is not None and error is None:
      message += f'Your function finished sucessfully with this result:\n\n`{description}`\n'
    elif description is None and error is None:
      message += 'Your function finished sucessfully with this result:\n\n`{}`\n'.format('None')
    elif description is None and error is not None:
      print(str(error))
      message += 'Your function finished with this error:\n\n`{}`\n'.format(str(error))
    
    message += '\nStart time: {}\nEnd time: {}\nElapsed time: {}' \
      .format(start.strftime('%H:%M:%S'), end.strftime('%H:%M:%S'), end - start)
    try:
      requests.post(
        f'https://api.telegram.org/bot{self.__api_token}/sendMessage',
        json={ "chat_id": self.__chat_id, "text": message, "parse_mode": "Markdown"}
      )
    except Exception as e:
      print('Error on sned message to telegram chat')
      print(e)