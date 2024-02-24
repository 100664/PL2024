import re

filename = "input.txt" 

with open(filename, 'r') as file:
    input = file.read()

regex = r'\bon\b|\d+|off|='
text = re.findall(regex, input, flags=re.IGNORECASE)

state = True
soma = 0

for char in text:
    if char.lower() == 'on':
        state = True
    elif char.lower() == 'off':
        state = False
    elif char.isdigit() and state:
        soma += int(char)
    elif char == '=':
        print(f'Soma: {soma}')
