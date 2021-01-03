from notifier import notify

@notify(duration=60, email="emmanu1962@gmail.com")
def test():
    return "TEST"

test()
# %%