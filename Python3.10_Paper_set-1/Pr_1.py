#1. Write output for the below statements, if you find any error please write the error.

print([] * 3)
#output:-[]

print(('a','b','c') * 2)
#output:- ('a','b','c','a','b','c')

print((2) ** 2)
#output:- 4

print([{}] * 2)
#output:-[{},{}]

print({3:1} *2)
#TypeError: unsupported operand type(s) for *: 'dict' and 'int'

print('123' + 2)
#TypeError: can only concatenate str (not "int") to str

print(['a','b','c'] + 'rf')
#TypeError: can only concatenate list (not "str") to list

print((2,4) ** 2)
#TypeError: unsupported operand type(s) for ** or pow(): 'tuple' and 'int'

z=['P','L','J']
z += 'SE'
print(z)
#['P', 'L', 'J', 'S', 'E']

