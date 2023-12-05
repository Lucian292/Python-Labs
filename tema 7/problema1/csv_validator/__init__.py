from reader import read_csv
from validator import CSVValidator

data_frame = read_csv('../csv_files/invalid.csv') # change this to valid.csv to see the difference

rules = {
    'column1': 'int',
    'column2': 'float',
    'column3': 'str',
}

validator = CSVValidator(rules)

validation_errors = validator.validate(data_frame)

if validation_errors:
    print("Validation Errors:")
    for column, error_message in validation_errors.items():
        print(f"{column}: {error_message}")
else:
    print("CSV file is valid.")
