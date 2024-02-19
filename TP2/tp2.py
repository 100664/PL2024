import re

def markdown_to_html(markdown):
    # Convertendo imagens
    markdown = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', markdown)

    # Convertendo links
    markdown = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', markdown)

    # Convertendo cabeçalhos
    markdown = re.sub(r'^#\s+(.*)$', r'\n<h1>\1</h1>', markdown, flags=re.MULTILINE)
    markdown = re.sub(r'^##\s+(.*)$', r'\n<h2>\1</h2>', markdown, flags=re.MULTILINE)
    markdown = re.sub(r'^###\s+(.*)$', r'\n<h3>\1</h3>', markdown, flags=re.MULTILINE)

    # Convertendo negrito
    markdown = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', markdown)

    # Convertendo itálicos
    markdown = re.sub(r'\*(.*?)\*', r'<i>\1</i>', markdown)

    # Substituindo lista numerada
    lines = markdown.split('\n')
    new_lines = []
    in_list = False
    for line in lines:
        if line.startswith('1. '):
            if not in_list:
                new_lines.append('<ol>')
                in_list = True
            line = '<li>' + line[3:] + '</li>'
        elif in_list and re.match(r'^\d+\. ', line):
            line = '</li><li>' + line[3:]
        elif in_list and not re.match(r'^\d+\. ', line):
            new_lines.append('</ol>')
            in_list = False
        new_lines.append(line)
    if in_list:
        new_lines.append('</ol>')
    markdown = '\n'.join(new_lines)

    return markdown


def convert_md_file_to_html(input_file, output_file):
    with open(input_file, 'r') as file:
        markdown_text = file.read()
    html_output = markdown_to_html(markdown_text)
    with open(output_file, 'w') as file:
        file.write(html_output)

input_file_path = 'exemplo.md'
output_file_path = 'exemplo.html'
convert_md_file_to_html(input_file_path, output_file_path)
convert_md_file_to_html('receita.md', 'receita.html')
print(f'Arquivo HTML "{output_file_path}" criado com sucesso!')
