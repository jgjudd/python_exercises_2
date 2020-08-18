from sys import argv
# argv brings in the imports via command line
# the next line unboxes argv and assigns them to variables
script, first, second, third = argv 

print('Your script is called: ', script)
print('Your first variable is:', first)
print('Your second variable is:', second)
print('You third variable is:', third)
