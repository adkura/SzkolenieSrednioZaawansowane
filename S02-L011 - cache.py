import time
import functools

@functools.lru_cache()
def Factorial(n):

    time.sleep(0.1)
    if n == 1:
        return 1
    else:
        return n*Factorial(n-1)

start = time.time()
for i in range(1,11):
    print('{}! = {}'.format(i, Factorial(i)))
stop = time.time()
print('Execution first time ', stop - start)

print(Factorial.cache_info())


'''
start2 = time.time()
for i in range(1, 11):
    print('{}! = {}'.format(i, Factorial(i)))
stop2 = time.time()
print('Second execution start time', start2)
print('Second execution stop time', stop2)
print('Execution second time', stop2 - start2)
'''