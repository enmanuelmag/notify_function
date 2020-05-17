from playsound import playsound
from pynotifier import Notification


def notifer_decorator(param):

    def wrapper_decorator(original_function):

        def wrapper_function(*args, **kwargs):

            print('Imprimiendo parametros pasado -> {}'.format(param))
            print('Inicio de llamado a la funcion')

            notification_to = Notification(
                'Function finished', 'Mensjae...')

            result = original_function(*args, **kwargs)

            notification_to.send()

            print('Fin de la ejecución')
            return result
        return wrapper_function

    return wrapper_decorator
