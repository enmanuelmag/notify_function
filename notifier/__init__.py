import os
import logging
import requests
import datetime
from os import path
from sys import platform
from pynotifier import Notification

# Catch any error of user function
logger = logging.Logger('catch_all')

# Path of icon's
ERROR_ICO = ''
SUCCESS_ICO = ''


def setIcons():
    '''
    Set repecticly path os ico's to use, but actually when the NotificatioN Class
    is created show a message (5, 'LoadImage', 'Acceso denegado.') for this reason
    this function doens't called

    So, actually this behavior doesn't work. If you found a solution
    please create a pull requests to check it. Thanks!
    '''
    if platform == "linux" or platform == "linux2":
        os_platform = 'linux'
        format_img = '.png'
    else:
        os_platform = 'windows'
        format_img = '.ico'

    ERROR_ICO = path.join('.', 'assets',
                          os_platform, 'error'+format_img)
    ERROR_ICO = os.path.abspath(ERROR_ICO)

    SUCCESS_ICO = path.join('.', 'assets',
                            os_platform, 'success'+format_img)
    SUCCESS_ICO = os.path.abspath(SUCCESS_ICO)


def notify(
    title='Function finished',
    msg='Your function has finished',
    duration=7,
    email=-1,
    urgency='normal'):
    '''
    This function recive some params to create the Notification and 
    show it when the user function finished

    Parameters:
    ------------
        title: (str): The title to use in the notification
        msg: (str): The message to usage in the notification
        duration: (int): time in seconds that notification will show

        urgency : (str): the urgency of notification. Options:
        URGENCY_LOW | URGENCY_NORMAL | URGENCY_CRITICAL
    '''
    # setIcons()
    def wrapper_decorator(original_function):

        def wrapper_function(*args, **kwargs):
            if urgency == 'low':
                urgency2 = Notification.URGENCY_LOW
            elif urgency == 'normal':
                urgency2 = Notification.URGENCY_NORMAL
            elif urgency == 'critial':
                urgency2 = Notification.URGENCY_CRITICAL
            else:
                urgency2 = Notification.URGENCY_NORMAL

            ico_result = SUCCESS_ICO
            isException = -1
            extra = -1
            result = None
            try:
                result = original_function(*args, **kwargs)
                extra = 'SUCCESFULLY - '
            except Exception as e:
                ico_result = ERROR_ICO
                extra = 'ERROR - '
                isException = e
            
            notification = Notification(
                extra + title, msg, duration, urgency2)
            
            try:
                notification.send()
                if email != -1:
                    if isException == -1:
                        subject = True 
                    else:
                        subject = False
                    requests.post('https://sender-msg.herokuapp.com/email/', 
                    json={
                        "email": email,
                        "subject": subject
                    })
            except Exception as e:
                raise e

            if isException != -1:
                raise isException
            else:
                return result

        return wrapper_function
    return wrapper_decorator
