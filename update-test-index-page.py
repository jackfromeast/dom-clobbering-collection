import os

# Base directory containing all the test folders
root_path = os.path.dirname(os.path.abspath(__file__))
assets_path = os.path.join(root_path, 'domc-gadgets-assets')

# Output file
index_file = os.path.join(assets_path, 'index.html')

# Function to read content from poc.html files and gather their paths
def read_poc_files(base_dir):
    poc_files_info = []
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file == 'poc.html':
                folder_name = os.path.basename(root)
                file_path = os.path.relpath(os.path.join(root, file), base_dir)
                poc_files_info.append((folder_name, file_path))
    return poc_files_info

# Function to generate index.html
def generate_index_html(base_dir):
    poc_files_info = read_poc_files(assets_path)
    with open(index_file, 'w') as index:
        index.write('<!DOCTYPE html>\n<html lang="en">\n<head>\n')
        index.write('  <meta charset="UTF-8">\n')
        index.write('  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
        index.write('  <title>DOM Clobbering Micro Benchmarks</title>\n')
        index.write('  <link rel="stylesheet" href="./styles/styles.css">\n')
        index.write('</head>\n<body>\n')
        index.write('<h1>DOM Clobbering Collection - Micro Benchmarks - Index</h1>\n')
        index.write('<section>\n')
        
        # Group poc files by their folders
        folder_dict = {}
        for folder_name, file_path in poc_files_info:
            if folder_name not in folder_dict:
                folder_dict[folder_name] = []
            folder_dict[folder_name].append(file_path)
        
        # Write each folder and its poc files to the index.html
        for folder_name, file_paths in folder_dict.items():
            index.write(f'  <h2>{folder_name} Test</h2><ul>\n')
            for file_path in file_paths:
                test_name = os.path.splitext(os.path.basename(file_path))[0]
                index.write(f'    <li><a href="{file_path}">Test: {test_name}</a></li>\n')
            index.write('  </ul>\n')
        
        index.write('</section>\n')
        index.write('</body>\n</html>\n')

# Run the script
generate_index_html(assets_path)
print(f'index.html has been generated in {assets_path}')
