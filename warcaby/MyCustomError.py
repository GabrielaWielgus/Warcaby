class MyCustomError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print('calling')
        if self.message:
            return 'CustomError, {0} '.format(self.message)
        else:
            return 'CustomError has been raised'


raise MyCustomError('Have problem')
