import requests

class Telegram(object):
  def __init__(self, api_token, chat_id, manual_call=False) -> None:
    self.__api_token = api_token
    self.__chat_id = chat_id
    if manual_call:
      self.description = 'Message:'
    else:
      self.description = 'Your function finished sucessfully with this result:'
  def send_message(self, title='', description='', error=None, start=None, end=None):
    if error is None:
      message = f'*{title}*  🚀\n'
    else:
      message = f'*{title}*  💥\n'
    if description is not None and error is None:
      message += f'{self.description}\n\n`{description}`\n'
    elif description is None and error is None:
      message += f'{self.description}\n\n`{"None"}`'
    elif description is None and error is not None:
      message += 'Your function finished with this error:\n\n`{}`\n'.format(str(error))
    if start is not None and end is not None:
      message += '\nStart time: {}\nEnd time: {}\nElapsed time: {}' \
        .format(start.strftime('%H:%M:%S'), end.strftime('%H:%M:%S'), end - start)
    try:
      requests.post(
        f'https://api.telegram.org/bot{self.__api_token}/sendMessage',
        json={ "chat_id": self.__chat_id, "text": message, "parse_mode": "Markdown"}
      )
    except Exception as e:
      print('Error on send message to telegram chat')
      raise e
