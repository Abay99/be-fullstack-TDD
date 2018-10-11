
def get_max(a, b):
    """
        return max number among a and b
    """
    if a > b: return a
    else: return b


def get_max_without_arguments():
    """
        raise TypeError exception with message 'missed arguments'
    """
    raise TypeError("missed arguments")

def get_max_with_one_argument(a):
    """
        return max value
    """
    return a

def get_max_with_many_arguments(*args):

    pass


def get_max_with_one_or_more_arguments(first, *args):
    pass


def get_max_bounded(*args, low, high):
    pass


def make_max(*, low, high):
    def inner(first, *args):
        pass

    return inner
