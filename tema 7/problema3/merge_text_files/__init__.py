from merger import merge_files

# Specify the order of files and the output file
file_paths = ['../txt_files/file3.txt', '../txt_files/file1.txt', '../txt_files/file2.txt']
output_file = '../txt_files/merged_output.txt'

# Customize the separator (optional, default is newline '\n')
custom_separator = '\n---\n'

# Merge files
merge_files(file_paths, output_file, custom_separator)
