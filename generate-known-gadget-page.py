import os
import re

# Function to extract the details from the markdown content
def parse_gadgets_from_markdown(markdown_file):
    with open(markdown_file, "r") as file:
        content = file.read()

    # Regular expressions for extracting sections
    gadget_pattern = re.compile(r"### (.*?)\n(.*?)#### Vulnerable Code\n```(.*?)```.*?#### Exploit\n```(.*?)```", re.DOTALL)
    gadgets = []
    
    matches = gadget_pattern.findall(content)
    
    for match in matches:
        title = match[0].strip()  # Extract the title
        references = re.findall(r"\+ (https?://[^\s]+)", match[1].strip())  # Extract multiple references
        vulnerable_code = match[2].strip()  # Extract vulnerable code
        exploit_code = match[3].strip()  # Extract exploit code
        
        gadget = {
            "title": title,
            "references": references,
            "vulnerable_code": vulnerable_code,
            "exploit_code": exploit_code
        }
        gadgets.append(gadget)

    return gadgets

# Function to generate the HTML PoC for each gadget
def generate_poc_html(gadget, index, output_folder):
    # Join multiple URLs into a proper HTML anchor list
    urls_html = "".join([f'<a href="{url}">{url}</a><br/>\n' for url in gadget['references']])

    html_template = f"""
    <html>
    <head>
    <title>DOM Clobbering Gadget {index+1}: {gadget['title']}</title>
    <p>SOURCE:</p>
    {urls_html}
    </head>
    <body>
    <p>Vulnerable Code:</p>
    {gadget['vulnerable_code']}
    <p>Exploit Code:</p>
    {gadget['exploit_code']}
    </body>
    </html>
    """

    filename = f"dom_clobbering_gadget_{index+1}.html"
    output_path = os.path.join(output_folder, filename)
    
    with open(output_path, "w") as file:
        file.write(html_template.strip())
    
    print(f"Generated {output_path}")

# Function to process the markdown and generate HTML PoCs
def process_markdown_and_generate_html(markdown_file, output_folder):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Parse gadgets from markdown file
    gadgets = parse_gadgets_from_markdown(markdown_file)
    
    # Generate HTML for each gadget
    for i, gadget in enumerate(gadgets):
        generate_poc_html(gadget, i, output_folder)

def read_poc_files(base_dir):
    poc_files_info = []
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.startswith('dom_clobbering_gadget') and file.endswith('.html'):
                file_path = os.path.relpath(os.path.join(root, file), base_dir)
                poc_files_info.append(file_path)
    return sorted(poc_files_info)

def generate_index_html(index_file, base_dir):
    poc_files_info = read_poc_files(base_dir)
    with open(index_file, 'w') as index:
        index.write('<!DOCTYPE html>\n<html lang="en">\n<head>\n')
        index.write('  <meta charset="UTF-8">\n')
        index.write('  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
        index.write('  <title>DOM Clobbering Gadgets PoC Index</title>\n')
        index.write('</head>\n<body>\n')
        index.write('<h1>DOM Clobbering Gadgets PoC Collection</h1>\n')
        index.write('<ul>\n')
        
        # Write each PoC HTML file as a link
        for file_path in poc_files_info:
            file_name = os.path.basename(file_path)
            test_name = file_name.replace('_', ' ').replace('.html', '')
            index.write(f'  <li><a href="{file_path}">{test_name}</a></li>\n')
        
        index.write('</ul>\n')
        index.write('</body>\n</html>\n')

    print(f'index.html has been generated at {index_file}')


markdown_file = "/home/jackfromeast/Desktop/TheHulk/dataset/dom-clobbering-collection/existing-gadgets.md" 
output_folder = "/home/jackfromeast/Desktop/TheHulk/dataset/dom-clobbering-collection/known-domc-gadgets"
process_markdown_and_generate_html(markdown_file, output_folder)


index_file = "/home/jackfromeast/Desktop/TheHulk/dataset/dom-clobbering-collection/known-domc-gadgets/index.html"
generate_index_html(index_file, output_folder)