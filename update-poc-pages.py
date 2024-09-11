import os
import re
import html 

# Directories for input and output
input_directory = './domc-gadgets'
output_directory = './domc-gadgets-assets/gadgets'

# Function to extract PoC section from the markdown file
def extract_poc_from_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    
    poc_section = {}

    # Use regular expressions to capture multi-line Library and Payload sections
    library_match = re.search(r'<!--Library-->\n(.*?)\n<!--Library-->', content, re.DOTALL)
    payload_match = re.search(r'<!--Payload-->\n(.*?)\n<!--Payload-->', content, re.DOTALL)

    if library_match:
        poc_section['Library'] = library_match.group(1).strip()
    
    if payload_match:
        poc_section['Payload'] = payload_match.group(1).strip()

    return poc_section

# Function to generate HTML files based on extracted PoC content
def generate_html_files(gadget_name, poc_content):
    os.makedirs(os.path.join(output_directory, gadget_name), exist_ok=True)
    
    poc_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DOM Clobbering Micro Benchmarks</title>
    <link rel="stylesheet" href="../styles/styles.css">
</head>
<body>
<h1>DOM Clobbering Collection - {gadget_name}</h1>

<section class="section">
  <div class="column">
  <p><span class="label">Payload</span><br><br>
  <pre>{html.escape(poc_content['Payload'])}</pre>
  {poc_content['Payload']}
  </div>
</section>

<section class="section">
  <div class="column">
  <p><span class="label">Library</span><br><br>
  <pre>{html.escape(poc_content['Library'])}</pre>
  {poc_content['Library']}
  </div>
</section>

</body>
</html>'''

    poc_benign_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DOM Clobbering Micro Benchmarks</title>
    <link rel="stylesheet" href="../styles/styles.css">
</head>
<body>

<h1>DOM Clobbering Collection - {gadget_name}</h1>

<section class="section">
  <div class="column">
  <p><span class="label">Library</span><br><br>
  <pre>{html.escape(poc_content['Library'])}</pre>
  {poc_content['Library']}
  </div>
</section>

</body>
</html>'''

    # Write poc.html and poc-benign.html
    output_path_poc = os.path.join(output_directory, gadget_name, 'poc.html')
    output_path_poc_benign = os.path.join(output_directory, gadget_name, 'poc-benign.html')
    
    with open(output_path_poc, 'w') as f:
        f.write(poc_html)
        
    with open(output_path_poc_benign, 'w') as f:
        f.write(poc_benign_html)

    print(f"Generated HTML files for {gadget_name}")

# Iterate over markdown files and generate HTML files
for filename in sorted(os.listdir(input_directory)):
    if filename.endswith('.md'):
        file_path = os.path.join(input_directory, filename)
        poc_content = extract_poc_from_file(file_path)
        if poc_content:
            gadget_name = filename.split('.')[0]
            generate_html_files(gadget_name, poc_content)

print("PoC web pages generated successfully.")
