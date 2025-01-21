import os

gadgets_input_directory = 'domc-gadgets'
html_input_directory = 'html-injection'
output_file = 'README.md'
gadgets_base_url = './domc-gadgets/'
html_base_url = './html-injection/'

readme_content = """# DOM Clobbering Collection

This repository maintains client-side libraries that are vulnerable to HTML injection or contain DOM Clobbering gadgets that can result in severe issues like XSS. This repository is actively maintained by [jackfromeast](https://github.com/jackfromeast) and [ishmeal](https://github.com/ishmeals).

> [!NOTE]
> Got new gadgets or HTML injections? Please feel free to create a Pull Request and join the house!

## What is DOM Clobbering?

_DOM Clobbering_ is a type of code-less injection attack on the web where attackers first inject a seemingly benign, scriptless HTML markup into a webpage. Then, the injected markup could be unexpectedly loaded by JavaScript through collided named property lookups on the `window` or `document` objects, potentially altering program execution and leading to serious security risks such as Cross-site Scripting (XSS) and Client-side Request Forgery (CSRF).

We also recommend checking out the following great websites, papers, and blog posts about DOM Clobbering:

+ Introductions:
  + The website [DOM Clobbering Wiki](https://domclob.xyz/) offers comprehensive information on attack techniques, vulnerability patterns, and defenses, along with tools for browser testing and payload generation.
  + The blog post "[Can HTML affect JavaScript? Introduction to DOM clobbering](https://aszx87410.github.io/beyond-xss/en/ch3/dom-clobbering/)" explains how HTML elements can influence JavaScript execution through DOM Clobbering.
+ Academic Papers:
  + The paper [It’s (DOM) Clobbering Time: Attack Techniques, Prevalence, and Defenses](https://publications.cispa.saarland/3756/1/sp23_domclob.pdf) by Soheil Khodayari and Giancarlo Pellegrino presents a systematic study of DOM Clobbering, uncovering various attack techniques, browser behaviors, and vulnerable code patterns, and evaluates existing countermeasures.
  + The paper [The DOMino Effect: Detecting and Exploiting DOM Clobbering Gadgets via Concolic Execution with Symbolic DOM]() by Zhengyu Liu et al. introduces a dynamic analysis tool using symbolic DOM modeling and concolic execution to detect and exploit DOM Clobbering gadgets at scale.
+ Cool Real-world Exploitations:
  + The blog post "[XSS in GMail’s AMP4Email via DOM Clobbering](https://research.securitum.com/xss-in-amp4email-dom-clobbering/)" by Michał Bentkowski details a real-world exploitation of DOM Clobbering to achieve XSS in Gmail's AMP4Email feature.
  + The blog post "[Go Go XSS Gadgets: Chaining a DOM Clobbering Exploit in the Wild](https://buer.haus/2024/02/23/go-go-xss-gadgets-chaining-a-dom-clobbering-exploit-in-the-wild/)" by Brett Buerhaus details how DOM Clobbering vulnerabilities can be chained to execute advanced XSS exploits.

## DOM Clobbering Gadgets

| Library | Stars | Version | Payloads | Impact | Found By | Status | CVE |
|:-------:|:-----:|:-------:|----------|:------:|:--------:|:------:|:---:|
"""


dom_clobbering_section = ""
html_injection_section = """\n## HTML Injection Vulnerabilities

The following libraries accept user input and output content as `type/html` with certain named attributes (e.g., `id` or `name`) preserved at different levels of capability. Using these libraries may expose web applications to HTML injection risks. Libraries may directly insert user input into the DOM, or the web application may retrieve the user input from the library and then add it to the DOM.

| Library | Stars | Version | Input | Sanitizer | Capability |
|:-------:|:-----:|:-------:|-------|:---------:|-------------------------|
"""

def convert_stars_to_number(stars_str):
    if 'K' in stars_str:
        return float(stars_str.replace('K', '')) * 1000
    elif 'M' in stars_str:
        return float(stars_str.replace('M', '')) * 1000000
    else:
        return 0
    
def extract_metadata(file_path, is_html_injection=False):
    with open(file_path, 'r') as file:
        content = file.read()
    metadata = {}
    lines = content.split('\n')
    for line in lines:
        if line.startswith("+ Library:"):
            metadata['Library'] = line.split(": ")[1]
        elif line.startswith("+ Stars:"):
            stars_str = line.split(": ")[1]
            metadata['Stars'] = stars_str
            metadata['StarsNumeric'] = convert_stars_to_number(stars_str)
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

def process_files(input_directory, is_html_injection=False):
    metadata_list = []
    for filename in sorted(os.listdir(input_directory)):
        if filename.endswith('.md'):
            file_path = os.path.join(input_directory, filename)
            metadata = extract_metadata(file_path, is_html_injection)
            if metadata:
                metadata['filename'] = filename  # Store the filename for later use
                metadata_list.append(metadata)
    
    metadata_list = sorted(metadata_list, key=lambda x: x.get('StarsNumeric', 0), reverse=True)
    
    section_content = ""
    for metadata in metadata_list:
        filename = metadata['filename']
        if is_html_injection:
            library_link = f"[{metadata['Library']}]({html_base_url}{filename})"
            section_content += f"| {library_link} | {metadata.get('Stars', 'N/A')} | {metadata.get('Version', 'N/A')} | {metadata.get('Input', 'N/A')} | {metadata.get('Sanitizer', 'N/A')} | {metadata.get('Capability', 'N/A')} |\n"
        else:
            library_link = f"[{metadata['Library']}]({gadgets_base_url}{filename})"
            section_content += f"| {library_link} | {metadata.get('Stars', 'N/A')} | {metadata.get('Version', 'N/A')} | {metadata.get('Payload', 'N/A')} | {metadata.get('Impact', 'N/A')} | {metadata.get('Foundby', 'N/A')} | {metadata.get('Status', 'Reported')} | {metadata.get('CVE', 'N/A')} |\n"
    
    return section_content

dom_clobbering_section += process_files(gadgets_input_directory, is_html_injection=False)
html_injection_section += process_files(html_input_directory, is_html_injection=True)


readme_content += dom_clobbering_section
readme_content += html_injection_section


with open(output_file, 'w') as file:
    file.write(readme_content)

print("README.md has been generated successfully.")
