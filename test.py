from notifier import notify

@notify(webhook_url='link')
def test():
    return 2

test()
