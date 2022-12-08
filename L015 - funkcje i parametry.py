def show_progress(how_many=0, character='*'):
    line = character * how_many
    print(line)


show_progress(10)
show_progress(15)
show_progress(30)

show_progress(10, '-')
show_progress(15, '+')