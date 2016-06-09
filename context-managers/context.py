class Context:

    def __init__(self):
        print('__init__() - created the Context object.')
    
    def __enter__(self):
        print('__enter__() - entering the "with" block.')
        return self

    def __exit__(self, a, b, c):
        print('__exit__() - exited the "with" block...doing this stuff now.')
        print('This __exit__() method received the Exception Type', a,
              'The Exception Value', b,
              'And the Exception TB', c)
        return True # So that the exception is not re-raised

if __name__ == '__main__':
    with Context() as c:
        print('Doing the work inside the "with" block.')
        print('The object passed in was:', c)
        raise Exception
