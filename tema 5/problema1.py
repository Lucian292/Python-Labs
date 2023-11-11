import os
import sys


def read_and_print_files(directory_path, file_extension):
    try:
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"The directory '{directory_path}' does not exist.")

        files = [file for file in os.listdir(directory_path) if file.endswith(file_extension)]

        if not files:
            raise FileNotFoundError(f"No files with the extension '{file_extension}' found in '{directory_path}'.")

        for file_name in files:
            file_path = os.path.join(directory_path, file_name)
            try:
                with open(file_path, 'r') as file:
                    print(f"Contents of {file_name}:\n{file.read()}\n{'=' * 30}\n")
            except Exception as e:
                print(f"Error reading file '{file_name}': {str(e)}")

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <directory_path> <file_extension>")
        sys.exit(1)

    directory_path = sys.argv[1]
    file_extension = sys.argv[2]

    read_and_print_files(directory_path, file_extension)

#exemplu de utilizare pt calculatorul meu: python problema1.py "D:\Universitate\python projects\tema 5\testScript1" .txt
