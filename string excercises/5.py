# a program that accepts values separated by a comma and produces a list and tuple
value = input('type a list of integers separated by commas: ')
list = value.split(',')
tuple = tuple(list)

print('List: ', list)
print('Tuple: ', tuple)
