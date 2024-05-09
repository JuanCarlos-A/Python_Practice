def volume_of_cube(side):
    if type(side) not in [int, float]:
        raise TypeError("The type of value is invalid")
    return side ** 3


if __name__ == '__main__':
    values = [2, 8, -3, 5j, 'ProgramandoAndo']

    for value in values:
        print('Cube Volume is : {}'.format(volume_of_cube(value)))