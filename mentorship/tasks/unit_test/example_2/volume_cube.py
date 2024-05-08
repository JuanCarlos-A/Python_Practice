def volume_of_cube(side):
    return side ** 3


if __name__ == '__main__':
    values = [2, 8, -3, 5j, 'ProgramandoAndo']

    for value in values:
        print('Cube Volume is : {}'.format(volume_of_cube(value)))