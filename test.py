from notifier import notify

@notify(duration=10)
def test():
    return "TEST"

test()
# %%