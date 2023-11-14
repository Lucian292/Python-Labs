import os
import sys


def calculate_total_size(directory_path):
    try:
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"The directory '{directory_path}' does not exist.")

        total_size = 0

        for root, dirs, files in os.walk(directory_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)

                total_size += os.path.getsize(file_path)

        print(f"Total size of all files in '{directory_path}': {total_size} bytes")

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]

    calculate_total_size(directory_path)
# Exemplu de utilizare pt calculatorul meu:  python problema3.py "D:\Universitate\python projects"