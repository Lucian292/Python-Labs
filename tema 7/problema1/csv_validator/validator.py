import pandas as pd


class CSVValidator:
    def __init__(self, rules=None):
        self.rules = rules or {}

    def validate(self, data_frame):
        errors = {}
        for column, rule in self.rules.items():
            if column not in data_frame.columns:
                errors[column] = "Column not found in the CSV."
            else:
                try:
                    data_frame[column].astype(rule)
                except ValueError:
                    errors[column] = f"Invalid data type. Expected: {rule}"

        return errors
