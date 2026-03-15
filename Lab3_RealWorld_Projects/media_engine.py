def monitor(func):
    def wrapper(*args, **kwargs):
        print("Processing Started")
        result = func(*args, **kwargs)
        print("Processing Completed")
        return result
    return wrapper


def signal_shutdown(power):

    if power == 0:
        print("System safely powered down.")
        return 1

    print("Current power:", power)

    return 1 + signal_shutdown(power - 1)


def play_count_stream(limit):

    for i in range(1, limit + 1):
        yield i * i