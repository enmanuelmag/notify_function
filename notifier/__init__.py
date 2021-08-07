from notifier.telegram_class import Telegram
from notifier.discord_class import Discord
from pynotifier import Notification
from datetime import datetime
from sys import platform
from os import path
import requests
import logging
import os

# Catch any error of user function
logger = logging.Logger('catch_all')

def setIcons():
    '''
    Set repecticly path os ico's to use, but actually when the NotificatioN Class
    is created show a message (5, 'LoadImage', 'Acceso denegado.') for this reason
    this function doens't called

    So, actually this behavior doesn't work. If you found a solution
    please create a pull requests to check it. Thanks!
    '''
    if platform == "linux" or platform == "linux2" or platform == "darwin":
      os_platform = 'linux'
      format_img = '.png'
    else:
      os_platform = 'windows'
      format_img = '.ico'

    ERROR_ICO = path.join('.', 'assets', os_platform, 'error'+format_img)
    ERROR_ICO = os.path.abspath(ERROR_ICO)

    SUCCESS_ICO = path.join('.', 'assets', os_platform, 'success'+format_img)
    SUCCESS_ICO = os.path.abspath(SUCCESS_ICO)
    return SUCCESS_ICO, ERROR_ICO


def notify(
  title='Function finished', msg='Your function has finished', duration=7, 
  email=None, urgency='normal', webhook_url=None, api_token=None, chat_id=None
):
  '''
  This function recive some params to create the Notification and 
  show it when the user function finished

  Parameters:
  ------------
    title: (str): The title to use in the notification

    msg: (str): The message to usage in the notification
    
    duration: (int): time in seconds that notification will show

    urgency : (str): the urgency of notification. Options: low, normal and critical

    webhook_url: (str): The url of the webhook to use, the notification will be send to the discord webhook
  '''
  SUCCESS_ICO, ERROR_ICO = setIcons()
  def wrapper_decorator(original_function):

    def wrapper_function(*args, **kwargs):
      result = None
      extra = None
      isException = None
      ico_result = SUCCESS_ICO
      
      try:
        start = datetime.now()
        result = original_function(*args, **kwargs)
        end = datetime.now()
        extra = 'SUCCESFULLY - '
      except Exception as e:
        end = datetime.now()
        ico_result = ERROR_ICO
        extra = 'ERROR - '
        isException = e

      notification = Notification(extra + title, msg, duration, urgency, ico_result)
      try:
        notification.send()
        if email is not None:
          if isException is None:
            subject = True 
          else:
            subject = False
          requests.post('https://sender-msg.herokuapp.com/email/', json={ "email": email, "subject": subject })
        if webhook_url is not None:
          discord = Discord(webhook_url)
          discord.send_message(title=extra + title, description=result, error=isException, start=start, end=end)
        if api_token is not None and chat_id is not None:
          telegram = Telegram(api_token, chat_id)
          telegram.send_message(title=extra + title, description=result, error=isException, start=start, end=end)
      except Exception as e:
        raise e
      if isException is not None:
        raise isException
      else:
        return result
    return wrapper_function
  return wrapper_decorator
