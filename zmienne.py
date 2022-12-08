a=20
b=c = 10

print(a, id(a))
print(b, id(b))
print(c, id(c))

print('-----------------------------------')
a=b=c = [1,2,3]
a.append(4)

print(a, id(a))
print(b, id(b))
print(c, id(c))
print('-----------------------------------')
x = 10
y = 10
y = y+1-1
y = y + 1234567890 - 1234567890
print(id(x), id(y))


