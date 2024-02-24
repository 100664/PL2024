import re

filename = "input.txt" 
output_file = "output.txt"

with open(filename, 'r') as file:
    stdin = file.read()

print("O arquivo foi lido com sucesso.")

regex = r'\bon\b|\d+|off|='
text = re.findall(regex, input, flags=re.IGNORECASE)

state = False 
soma = 0

output_lines = [] 
for char in text:
    if char.lower() == 'on':
        state = True
    elif char.lower() == 'off':
        state = False
    elif char.isdigit() and state:
        soma += int(char)
    elif char == '=':
        output_lines.append(f'Soma: {soma}') 

with open(output_file, 'w') as output:
    for line in output_lines:
        output.write(line + '\n')
