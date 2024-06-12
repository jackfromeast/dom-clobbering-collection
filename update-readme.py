import os

# Directory containing the library files
input_directory = 'domc-gadgets'
output_file = 'README.md'
github_base_url = 'https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/'

# Initialize the README content
readme_content = """# DOM Clobbering Collection

In this repo, we collect a list of client-side libraries that are either vulnerable to HTML injection or contain DOM Clobbering gadgets that lead to severe consequences, e.g., XSS.

## HTML Injection

## DOM Clobbering Gadgets

| Library | Version | Payloads | Impact | Found By |
|:-------:|:-------:|----------|:------:|:--------:|
"""

# Function to extract metadata from a file
def extract_metadata(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    metadata = {}
    lines = content.split('\n')
    for line in lines:
        if line.startswith("+ Library:"):
            metadata['Library'] = line.split(": ")[1]
        elif line.startswith("+ Version:"):
            metadata['Version'] = line.split(": ")[1]
        elif line.startswith("+ Payload:"):
            metadata['Payload'] = line.split(": ")[1]
        elif line.startswith("+ Impact:"):
            metadata['Impact'] = line.split(": ")[1]
        elif line.startswith("+ Foundby:"):
            metadata['Foundby'] = line.split(": ")[1]
    return metadata

# Iterate over each file in the directory
for filename in os.listdir(input_directory):
    if filename.endswith('.md'):
        file_path = os.path.join(input_directory, filename)
        metadata = extract_metadata(file_path)
        if metadata:
            library_link = f"[{metadata['Library']}]({github_base_url}{filename})"
            readme_content += f"| {library_link} | {metadata['Version']} | {metadata['Payload']} | {metadata['Impact']} | {metadata['Foundby']} |\n"

# Write the content to README.md
with open(output_file, 'w') as file:
    file.write(readme_content)

print("README.md has been generated successfully.")
