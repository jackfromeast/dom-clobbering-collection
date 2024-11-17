import os

# Base directory containing all the test folders
root_path = os.path.dirname(os.path.abspath(__file__))
assets_path = os.path.join(root_path, 'domc-gadgets-assets', 'gadgets')

# Output files
index_file = os.path.join(assets_path, 'index.html')
index_benign_file = os.path.join(assets_path, 'index-benign.html')

# Function to read content from specific PoC files and gather their paths
def read_poc_files(base_dir, target_file):
    poc_files_info = []
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file == target_file:
                folder_name = os.path.basename(root)
                file_path = os.path.relpath(os.path.join(root, file), base_dir)
                poc_files_info.append((folder_name, file_path))
    return poc_files_info

# Function to generate index.html
def generate_index_html(base_dir, output_file, target_file, title):
    poc_files_info = read_poc_files(base_dir, target_file)
    with open(output_file, 'w') as index:
        index.write('<!DOCTYPE html>\n<html lang="en">\n<head>\n')
        index.write('  <meta charset="UTF-8">\n')
        index.write('  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
        index.write(f'  <title>{title}</title>\n')
        index.write('  <link rel="stylesheet" href="./styles/styles.css">\n')
        index.write('</head>\n<body>\n')
        index.write(f'<h1>{title}</h1>\n')
        index.write('<section>\n')
        
        # Group poc files by their folders
        folder_dict = {}
        for folder_name, file_path in poc_files_info:
            if folder_name not in folder_dict:
                folder_dict[folder_name] = []
            folder_dict[folder_name].append(file_path)
        
        # Write each folder and its PoC files to the index.html
        for folder_name, file_paths in sorted(folder_dict.items()):
            index.write(f'  <h3>{folder_name} Test</h3><ul>\n')
            for file_path in file_paths:
                test_name = os.path.splitext(os.path.basename(file_path))[0]
                if 'squirt' in file_path:
                    index.write(f'    <li><a href="{file_path}?sq-dev">{test_name}</a></li>\n')
                else:
                    index.write(f'    <li><a href="{file_path}">{test_name}</a></li>\n')
            index.write('  </ul>\n')
        
        index.write('</section>\n')
        index.write('</body>\n</html>\n')

# Generate both index.html and index-benign.html
generate_index_html(assets_path, index_file, 'poc.html', 'DOM Clobbering Collection - Micro Benchmarks - Index')
print(f'index.html has been generated in {assets_path}')

generate_index_html(assets_path, index_benign_file, 'poc-benign.html', 'DOM Clobbering Collection - Benign Micro Benchmarks - Index')
print(f'index-benign.html has been generated in {assets_path}')
