import time

def wrapper_time(a_function):
    def a_wrapper_function(*args, **kwargs):
        time_start = time.time()
        v = a_function(*args, **kwargs)
        time_stop = time.time()
        print('Funkcja "{}" wykonan w czasie: {}'.format(a_function.__name__, time_stop - time_start))
        return v
    return a_wrapper_function

def get_sequence(n):

    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i) ) /2
        return v

wrapper_get_sequence = wrapper_time(get_sequence)

print(wrapper_get_sequence(18))

