import os


def rename_files_with_sequential_prefix(directory_path):
    try:
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"The directory '{directory_path}' does not exist.")

        files = [file for file in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, file))]

        if not files:
            raise FileNotFoundError(f"No files found in '{directory_path}'.")

        for i, file_name in enumerate(files, start=1):
            original_path = os.path.join(directory_path, file_name)
            new_name = f"file{i}{os.path.splitext(file_name)[1]}"
            new_path = os.path.join(directory_path, new_name)

            os.rename(original_path, new_path)
            print(f"Renamed: {original_path} -> {new_path}")

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    directory_path = r"D:\Universitate\python projects\tema 5\testScript2"

    rename_files_with_sequential_prefix(directory_path)
