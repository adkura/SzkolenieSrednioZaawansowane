def calculate_paint(efficency_ltr_per_m2, *args):
    sumam2 = sum(args)
    return efficency_ltr_per_m2 * sumam2


print(calculate_paint(1,13, 23, 12, 23))

pow = [23 ,4 ,24 ,12 ,34]

print(calculate_paint(1, *pow))


def log_it(*args):
    file_path = r'/home/adam/temp/log_it.txt'
    with open(file_path, 'a') as f:
        for a in args:
            f.write(a)
            f.write(' ')
        f.write('\n')


log_it('Starting processing forecasting')
log_it('ERROR', 'Not enough data', 'invoices', '2020')




