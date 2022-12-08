text_list = ['x','xxx','xxxxx','xxxxxxx','']

f = lambda t: len(t)

print(f('długośc ciągu znaków'))

print(list(map(f, text_list)))

print(list(map(lambda s: len(s), text_list)))