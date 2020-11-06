from notifier_function.notifier import notifer_decorator as nd


@nd(duration=60)
def test():
    return True


test()
