import os

# Directories containing the gadget and HTML injection files
gadgets_input_directory = 'domc-gadgets'
html_input_directory = 'html-injection'
output_file = 'README.md'
github_base_url = './domc-gadgets/'

# Initialize the README content
readme_content = """# DOM Clobbering Collection

This repository lists client-side libraries that are vulnerable to HTML injection or contain DOM Clobbering gadgets that can result in severe issues like XSS.

## DOM Clobbering Gadgets

| Library | Stars | Version | Payloads | Impact | Found By | Status | CVE |
|:-------:|:-----:|:-------:|----------|:------:|:--------:|:------:|:---:|
"""

# DOM Clobbering section content placeholder
dom_clobbering_section = ""

# HTML Injection section content placeholder
html_injection_section = """\n## HTML Injection Vulnerabilities

The following libraries accept user input and output content as `type/html` with certain named attributes (e.g., `id` or `name`) preserved at different levels of capability. Using these libraries may expose web applications to HTML injection risks. Libraries may directly insert user input into the DOM, or the web application may retrieve the user input from the library and then add it to the DOM.

| Library | Stars | Version | Input | Sanitizer | Capability | Status | CVE |
|:-------:|:-----:|:-------:|-------|:---------:|-------------------------|:------:|:---:|
"""

# Function to extract metadata from a file
def extract_metadata(file_path, is_html_injection=False):
    with open(file_path, 'r') as file:
        content = file.read()
    metadata = {}
    lines = content.split('\n')
    for line in lines:
        if line.startswith("+ Library:"):
            metadata['Library'] = line.split(": ")[1]
        elif line.startswith("+ Stars:"):
            metadata['Stars'] = line.split(": ")[1]
        elif line.startswith("+ Version:"):
            metadata['Version'] = line.split(": ")[1]
        elif is_html_injection:
            if line.startswith("+ Input:"):
                metadata['Input'] = line.split(": ")[1]
            elif line.startswith("+ Sanitizer:"):
                metadata['Sanitizer'] = line.split(": ")[1]
            elif line.startswith("+ Capability:"):
                metadata['Capability'] = line.split(": ")[1]
        else:
            if line.startswith("+ Payload:"):
                metadata['Payload'] = line.split(": ")[1]
            elif line.startswith("+ Impact:"):
                metadata['Impact'] = line.split(": ")[1]
            elif line.startswith("+ Foundby:"):
                metadata['Foundby'] = line.split(": ")[1]
        if line.startswith("+ CVE:"):
            metadata['CVE'] = line.split(": ")[1]
        elif line.startswith("+ Status:"):
            metadata['Status'] = line.split(": ")[1]
    return metadata

# Function to process files and append content to the corresponding section
def process_files(input_directory, is_html_injection=False):
    section_content = ""
    for filename in sorted(os.listdir(input_directory)):
        if filename.endswith('.md'):
            file_path = os.path.join(input_directory, filename)
            metadata = extract_metadata(file_path, is_html_injection)
            if metadata:
                library_link = f"[{metadata['Library']}]({github_base_url}{filename})"
                if is_html_injection:
                    section_content += f"| {library_link} | {metadata.get('Stars', 'N/A')} | {metadata.get('Version', 'N/A')} | {metadata.get('Input', 'N/A')} | {metadata.get('Sanitizer', 'N/A')} | {metadata.get('Capability', 'N/A')} | {metadata.get('Status', 'N/A')} | {metadata.get('CVE', 'N/A')} |\n"
                else:
                    section_content += f"| {library_link} | {metadata.get('Stars', 'N/A')} | {metadata.get('Version', 'N/A')} | {metadata.get('Payload', 'N/A')} | {metadata.get('Impact', 'N/A')} | {metadata.get('Foundby', 'N/A')} | {metadata.get('Status', 'N/A')} | {metadata.get('CVE', 'N/A')} |\n"
    return section_content

# Process DOM Clobbering Gadget files first
dom_clobbering_section += process_files(gadgets_input_directory, is_html_injection=False)

# Process HTML Injection files next
html_injection_section += process_files(html_input_directory, is_html_injection=True)

# Combine sections into final README content
readme_content += dom_clobbering_section
readme_content += html_injection_section

# Write the content to README.md
with open(output_file, 'w') as file:
    file.write(readme_content)

print("README.md has been generated successfully.")
