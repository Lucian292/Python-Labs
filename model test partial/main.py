import re
import os


def parse_csv(file_path, column_name):
    try:
        if not os.path.isfile(file_path):
            print("[ERROR] - file not found")
            return

        with open(file_path, 'r') as file:
            lines = file.readlines()

            header = lines[0].strip().split(',')

            header_lower = [col.lower() for col in header]

            if column_name.lower() not in header_lower:
                print("[ERROR] - unknown column name")
                return

            column_index = header_lower.index(column_name.lower())

            word_count = {}

            line_number = 2
            for line in lines[1:]:
                if line.strip():
                    if len(re.split(r'\s*,\s*', line.strip())) != len(header):
                        print(f"[ERROR] - invalid format - different words on line {line_number}")
                        return

                    word = re.split(r'\s*,\s*', line.strip())[column_index].lower()

                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1

                line_number += 1

            if len(header) != len(set(header_lower)):
                print("[ERROR] - invalid format - duplicate columns")
                return

            print("[OK]")
            for word, count in sorted(word_count.items(), key=lambda x: (-x[1], x[0])):
                print(word)

    except Exception as e:
        print(f"[ERROR] - {e}")


if __name__ == "__main__":
    if len(os.sys.argv) != 3:
        print("Usage: python csvparser.py <path_to_csv_file> <column_name>")
    else:
        file_path = os.sys.argv[1]
        column_name = os.sys.argv[2]
        parse_csv(file_path, column_name)
