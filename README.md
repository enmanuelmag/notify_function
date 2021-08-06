# Notifier Function Status
This library uses a decorator to show a toast in your screen or send you a email when your function has finished

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
- **msg**: the message of toast notification, by default is: `Your function has finished`.
- **duration**: the time, in seconds, that the nottications will show, by default is `8`.
- **urgency**: the urgency of the notifcation. By defualt is `normal`. The options are:
  - low.
  - normal.
  - critical.

Made with ❤️ by [Enmanuel Magallanes](https://cardor.dev)
