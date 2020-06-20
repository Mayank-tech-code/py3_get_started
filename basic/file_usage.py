import os

output_file = open('output.txt','w')
output_file.write('First Line\n')
output_file.write('Second Line\n')
output_file.close()

input_file = open('output.txt','r')
contents = input_file.read()
print(contents)
input_file.close()