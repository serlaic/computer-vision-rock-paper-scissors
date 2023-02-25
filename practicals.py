import time

def start_end(func):
    def wrapper(x):
        time_0 = time.time()
        func(x)
        time_1 = time.time()
        print(f'It took {time_1 - time_0} seconds to run')
    return wrapper

@start_end
def my_function(x):
    for i in range(x):
        test = 'Test'
    return test

my_function(100000)
