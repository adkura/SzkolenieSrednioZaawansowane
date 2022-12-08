ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

routgen = ((start, stop) for start in ports for stop in ports)
i = 1
for (start, stop) in routgen:
    print('{} - {}'.format(start, stop))
    i +=1

print('występuje {} możliwych połączeń'.format(i))

# routgen = ((start, stop) for start in ports for stop in ports if start != stop)
# i = 1
# while True:
#     try:
#         print(next(routgen))
#         i += 1
#     except StopIteration:
#         print('-'*30)
#         print('występuje {} możliwych połączeń'.format(i))
#         break


# routgen = ((start, stop) for start in ports for stop in ports if start < stop)
# i = 1
# while True:
#     try:
#         print(next(routgen))
#         i += 1
#     except StopIteration:
#         print('-'*30)
#         print('występuje {} możliwych połączeń'.format(i))
#         break
#
