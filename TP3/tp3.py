import re

filename = "input.txt"  
output_file = "output.txt" 

with open(filename, 'r') as file:
    stdin = file.read()

print("O arquivo foi lido com sucesso.")

symbols_regex = r'\bon\b|\d+|off|='
symbols = re.findall(symbols_regex, stdin, flags=re.IGNORECASE)

state = False 
current = 0

output_lines = []

for symbol in symbols:
    if symbol.lower() == 'on':
        state = True
    elif symbol.lower() == 'off':
        state = False
    elif symbol.isdigit() and state:
        current += int(symbol)
    elif symbol == '=':
        output_lines.append(f'Soma: {current}')

with open(output_file, 'w') as output:
    for line in output_lines:
        output.write(line + '\n')
