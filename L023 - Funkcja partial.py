import requests
import os
import functools

def save_url_file(url, dir, file, msg):
    print(msg.format(file))

    r = requests.get(url, stream=True)
    file_path = os.path.join(dir, file)

    with open(file_path, "wb") as f:
        f.write(r.content)


save_url_to_dir = functools.partial(save_url_file, dir = '/home/adam/temp', msg = 'Pleace wait: {}')

msg = "Please wait - the file {} will be downloaded"

url = 'http://mobilo24.eu/spis'
dir = '/home/adam/temp/'
file = 'spis.html'
#save_url_file(url, dir, file, msg)
save_url_to_dir(url = url, file = file)



url = 'https://www.mobilo24.eu/wp-content/uploads/2015/11/Mobilo_logo_kolko_512-565b1626v1_site_icon.png'
dir = '/home/adam/temp/'
file = 'logo.png'
#save_url_file(url, dir, file, msg)
save_url_to_dir(url = url, file = file)