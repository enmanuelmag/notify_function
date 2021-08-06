from discord_webhook import DiscordWebhook, DiscordEmbed
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


def notify(title='Function finished', msg='Your function has finished', duration=7, email=None, urgency='normal', webhook_url=None):
  '''
  This function recive some params to create the Notification and 
  show it when the user function finished

  Parameters:
  ------------
    title: (str): The title to use in the notification

    msg: (str): The message to usage in the notification
    
    duration: (int): time in seconds that notification will show

    urgency : (str): the urgency of notification. Options: low, normal and critical
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
          if isException is not None:
            subject = True 
          else:
            subject = False
          requests.post('https://sender-msg.herokuapp.com/email/', json={ "email": email, "subject": subject })
        if webhook_url is not None:
          discord = Discord(webhook_url)
          discord.send_message(title=extra + title, description=result, error=isException, start=start, end=end)
      except Exception as e:
        raise e
      if isException is not None:
        raise isException
      else:
        return result
    return wrapper_function
  return wrapper_decorator


class Discord(object):
  def __init__(self, webhook_url):
    self.webhook_url = webhook_url
    self.webhook = DiscordWebhook(url=webhook_url)
    self.error_img = 'https://raw.githubusercontent.com/enmanuel-mag/notify_function/master/notifier/assets/linux/error.png'
    self.success_img = 'https://raw.githubusercontent.com/enmanuel-mag/notify_function/master/notifier/assets/linux/success.png'
    self.logo = 'https://raw.githubusercontent.com/enmanuel-mag/notify_function/master/notifier/assets/logo.png'
  def send_message(self, title='', description='', error=None, start=None, end=None):
    color = '44AA00'

    if error is not None:
      color = 'BB250C'
    delta = end - start
    if description is not None and error is None:
      description = f'Your function finished sucessfully with this result:\n```{description}```'
    elif description is None and error is None:
      description = 'Your function finished sucessfully with this result:\n```{}```'.format('None')
    elif description is None and error is not None:
      description = 'Your function finished with this error:\n```{}```'.format(error)

    embed = DiscordEmbed(title=title, description=description, color=color)
    #embed.set_image(url=img_msg)
    #embed.set_thumbnail(url=img_msg)
    #embed.set_footer(text='Notify function')
    #embed.set_timestamp()

    embed.add_embed_field(name='Start time', value=start.strftime('%H:%M:%S'))
    embed.add_embed_field(name='End time', value=end.strftime('%H:%M:%S'))
    embed.add_embed_field(name='Elapsed time', value=f'{delta}')

    embed.set_author(name='Notify Function', url='https://github.com/enmanuel-mag', icon_url=self.logo)

    self.webhook.add_embed(embed)
    self.webhook.execute()
