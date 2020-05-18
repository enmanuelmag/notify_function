import os
import logging
import requests
from os import path
from sys import platform
from pynotifier import Notification

# Catch any error of user function
logger = logging.Logger('catch_all')

# Path of icon's
ERROR_ICO = ''
SUCCESS_ICO = ''


def set_icons():
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

    ERROR_ICO = path.join('notify_end', 'assets',
                          os_platform, 'error'+format_img)
    ERROR_ICO = os.path.abspath(ERROR_ICO)

    SUCCESS_ICO = path.join('notify_end', 'assets',
                            os_platform, 'success'+format_img)
    SUCCESS_ICO = os.path.abspath(SUCCESS_ICO)


def send_email(email, subject, text, api):
    '''
    This function send a email with information of the fucntion

    Parameters:
    ---------
        email: (str): email address to send information
        subject: (str): status of the function
        text: (str): information of the function
    '''
    try:
        response = requests.post(
            "https://api.mailgun.net/v3/sandbox49eebe67a3eb430e94669e2220f4ef84.mailgun.org/messages",
            auth=("api", api),
            data={"from": "Notifier Function Status <notifierfunction@gmail.com>",
                  "to": email,
                  "subject": "Hello! Your function has finished {}".format(subject),
                  "text": text})
    except Exception as e:
        logger.error('Failed to send email: \n' +
                     str(e), exc_info=True)


def notifer_decorator(title='Function finished',
                      msg='Your function has finished',
                      duration=8,
                      result_info=False,
                      urgency=Notification.URGENCY_NORMAL,
                      email='',
                      api=''
                      ):
    '''
    This function recive some params to create the Notification and 
    show it when the user function finished

    Parameters:
    ------------
        title: (str): The title to use in the notification
        msg: (str): The message to usage in the notification
        duration: (int): time in seconds that notification will show
        result_info: (bool): add your return funtion to text in the email
        urgency : (str): the urgency of notification. Options:
        URGENCY_LOW | URGENCY_NORMAL | URGENCY_CRITICAL
        api: (str): you api key of Mailgun
    '''
    # set_icons()

    def wrapper_decorator(original_function):

        def wrapper_function(*args, **kwargs):

            result_email = 'Your function has finished. {}'.format(msg)
            ico_result = SUCCESS_ICO

            subject = ''
            extra = ''
            try:
                result = original_function(*args, **kwargs)
                extra = ' - (success)'
                subject = 'successfully'
                if result_info:
                    result_email += str(result)
            except Exception as e:

                ico_result = ERROR_ICO
                extra = ' - (error)'
                subject = 'with a error'
                result = str(e)
                logger.error('Failed to do something: \n' +
                             str(e), exc_info=True)

            notification = Notification(
                title+extra, msg, duration, urgency)

            if email != '':
                if api != '':
                    send_email(email, subject, result_email, api)
                else:
                    print(
                        'You must pass a api of Mailgun to sned emails. Check on https://www.mailgun.com')

            notification.send()

            return result

        return wrapper_function

    return wrapper_decorator
