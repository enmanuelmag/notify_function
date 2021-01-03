# Notifier Function Status
This library use a decorator to show a toast in your screen.

## Requeriments

Please install this packages by yourself depending you OS:

- Windows: ```pip3 install win10toast```
- Ubuntu: ```apt-get install libnotify-bin``` (if don't work try searching how install notify-send for your distro of Linux)

## Usage

All that you need is use a decorator and specific some parameters, next explain it:

Import: `from notifier import notify`

Decorator to use: `@notify()`

### Parameters

- **title**: the title of toast notification, by defult is: Function finished.
- **msg**: the message of toast notification, by default is: `Your function has finished`.
- **duration**: the time, in seconds, that the nottications will show, by default is 8.
- **urgency**: the urgency of the notifcation. By defualt is `normal`. The options are:
  - low.
  - normal.
  - critial.
