import os

files_to_process = [
    r"/home/adam/temp/math_sin_square.py",
    r"/home/adam/temp/math_square_root.py"
]

for f in files_to_process:
    print(os.path.basename(f))
    file = open(f, 'r')
    source = file.read()
    file.close()
    exec(source)


