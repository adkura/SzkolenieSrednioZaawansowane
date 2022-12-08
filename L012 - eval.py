import math

formula = '3*x**2+2*x-4'

argument_list = []

k = 0.1

for i in range(100):
    argument_list.append(k)
    k += 0.1

for x in argument_list:
    print('{0:3.1f}  -  {1:6.2f}'.format(x, eval(formula)))

