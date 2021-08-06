from notifier import notify

@notify(webhook_url='https://discord.com/api/webhooks/796406472459288616/PAkiGGwqe0_PwtBxXYQvOzbk78B4RQP6VWRkvpBtw6Av0sc_mDa3saaIlwVPFjOIeIbt')
def test():
    return 2

test()
