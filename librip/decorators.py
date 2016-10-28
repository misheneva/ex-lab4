def print_result(printable_func):

    def decorated(*args):
        print(printable_func.__name__)
        if type(printable_func(*args)) == list:
            for i in printable_func(*args):
                print(i)
        elif type(printable_func(*args)) == dict:
            for key, val in printable_func(*args).items():
                print('{} = {}'.format(key, val))
        else:
            print(printable_func(*args))

    return decorated
