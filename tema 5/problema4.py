import os
import sys


def count_files_by_extension(directory_path):
    try:
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"The directory '{directory_path}' does not exist.")

        files = [file for file in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, file))]

        if not files:
            raise FileNotFoundError(f"No files found in '{directory_path}'.")

        extension_counts = {}

        for file_name in files:
            _, extension = os.path.splitext(file_name)
            extension = extension.lower()

            extension_counts[extension] = extension_counts.get(extension, 0) + 1

        print(f"File counts by extension in '{directory_path}':")
        for extension, count in extension_counts.items():
            print(f"{extension}: {count} file(s)")

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]

    count_files_by_extension(directory_path)
# Exemplu de utilizare pt calculatorul meu:  python problema4.py "D:\Universitate\python projects\tema 5\testScript4