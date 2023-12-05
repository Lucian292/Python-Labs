def merge_files(file_paths, output_file, custom_separator='\n'):
    try:
        with open(output_file, 'w') as merged_file:
            for file_path in file_paths:
                with open(file_path, 'r') as current_file:
                    merged_file.write(current_file.read())
                    merged_file.write(custom_separator)
        print(f'Merged files into {output_file} successfully.')
    except Exception as e:
        print(f'Error: {e}')
