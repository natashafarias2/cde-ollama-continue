import re

def validate_date(date):
    # Aceita: DD/MM/YYYY, DD-MM-YYYY, DD MM YYYY
    pattern = r"\b(0?[1-9]|1[0-2])[\/\-\s](0?[1-9]|[12][0-9]|3[01])[\/\-\s](\d{4})\b"
    if re.match(pattern, date):
        return True
    else:
        return False

date = input("Enter a date (DD/MM/YYYY): ")
if validate_date(date):
    print(f"{date} is a valid date!")
else:
    print(f"{date} is not a valid date.")
