import os
import urllib.request

data_dir = r'/home/adam/temp'
pages = [{ 'name': 'mobilo',      'url': 'http://www.mobilo24.eu/'},

         { 'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/' },

         { 'name': 'kursy',       'url': 'http://www.kursyonline24.eu/'} ]


for page in pages:
    try:
        fname = "{}.html".format(page['name'])
        path = os.path.join(data_dir, fname)
        print(path)
        urllib.request.urlretrieve(page['url'], path)
        print('...done')
    except:
        print('wystąpił błąd przy ściąganiu strony {}'.format(page['name']))
else:
    print('Successfull')



