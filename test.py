#
#

from jok_inputs import input_float, input_int, input_str


a = input_int('Input integer A: ')
b = input_float(message='Input floating B: ')
c = input_str('Input string C: ')

print(f'A = {a}, {type(a)}')
print(f'B = {b}, {type(b)}')
print(f'C = {c}, {type(c)}')