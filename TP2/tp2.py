import re

def convert_images(markdown):
    return re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', markdown)

def convert_links(markdown):
    return re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', markdown)

def convert_headers(markdown):
    markdown = re.sub(r'^#\s+(.*)$', r'<h1>\1</h1>', markdown, flags=re.MULTILINE)
    markdown = re.sub(r'^##\s+(.*)$', r'<h2>\1</h2>', markdown, flags=re.MULTILINE)
    markdown = re.sub(r'^###\s+(.*)$', r'<h3>\1</h3>', markdown, flags=re.MULTILINE)
    return markdown

def convert_bold(markdown):
    return re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', markdown)

def convert_italics(markdown):
    return re.sub(r'\*(.*?)\*', r'<i>\1</i>', markdown)

def convert_numbered_list(markdown):
    html_output = []
    in_ordered_list = False
    in_unordered_list = False

    for line in markdown.split('\n'):
        # Ordered List
        ordered_list_match = re.match(r'^(\d+\.\s)(.*)', line)
        if ordered_list_match:
            if not in_ordered_list:
                html_output.append('<ol>')
                in_ordered_list = True
            html_output.append(f'<li>{ordered_list_match.group(2)}</li>')
            continue

        # Unordered List
        unordered_list_match = re.match(r'^([*+-]\s)(.*)', line)
        if unordered_list_match:
            if not in_unordered_list:
                html_output.append('<ul>')
                in_unordered_list = True
            html_output.append(f'<li>{unordered_list_match.group(2)}</li>')
            continue

        # Closing Ordered List
        if in_ordered_list and not ordered_list_match:
            html_output.append('</ol>')
            in_ordered_list = False

        # Closing Unordered List
        if in_unordered_list and not unordered_list_match:
            html_output.append('</ul>')
            in_unordered_list = False

        # Other Markdown to HTML conversions
        line = convert_images(line)
        line = convert_links(line)
        line = convert_headers(line)
        line = convert_bold(line)
        line = convert_italics(line)

        # Append to output
        html_output.append(line)

    # Close any remaining lists
    if in_ordered_list:
        html_output.append('</ol>')
    if in_unordered_list:
        html_output.append('</ul>')

    return '\n'.join(html_output)

def markdown_to_html(markdown):
    markdown = convert_images(markdown)
    markdown = convert_links(markdown)
    markdown = convert_headers(markdown)
    markdown = convert_bold(markdown)
    markdown = convert_italics(markdown)
    markdown = convert_numbered_list(markdown)
    return markdown

def convert_md_file_to_html(input_file, output_file):
    with open(input_file, 'r') as file:
        markdown_text = file.read()
    html_output = markdown_to_html(markdown_text)
    with open(output_file, 'w') as file:
        file.write(html_output)


convert_md_file_to_html('exemplo.md', 'exemplo.html')
convert_md_file_to_html('receita.md', 'receita.html')
print(f'Arquivo HTML exemplo.html criado com sucesso!')
print(f'Arquivo HTML receita.html criado com sucesso!')
