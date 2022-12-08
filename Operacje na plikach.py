import os

def ReadFile(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        word_count = len(content.split())
    return word_count


filepath = r'/home/adam/temp/lekcja4.txt'

if not os.path.isfile(filepath):
    pass
else:
    print('There are {} words in the file {}'.format(ReadFile(filepath), filepath))

os.path.isfile(filepath) and print('There are {} words in the file {}'.format(ReadFile(filepath), filepath))

