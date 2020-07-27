
def try_except(method):
    '''
    This function will be used a decorator
    Prints out exception if any
    '''
    def catch_error(x):
        try:
            return method(x)
        except Exception as ex:
            print(ex)

    return catch_error