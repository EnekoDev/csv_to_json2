import os
import csv
import json

CSV_URL = os.environ['CSV_URL']
JSON_URL = os.environ['JSON_URL']

def str_to_bool(value):
    if isinstance(value, str):
        return value.lower() == 'true'
    return value

# As the process is quite slow I placed some messages to know that the script is running as I tend to overthink stuff too much
print("BEGIN")

all_users = []

with open(CSV_URL, mode="r") as csvfile:
    reader = csv.DictReader(csvfile)
    
    count = 14  # The row from which you start adding the data, in this case from row 15 onwards
    
    for row in reader:
        count += 1
        id_key = str(count)

        user_data = {}
        
        for key, value in row.items():
            if value.isdigit():
                user_data[key] = int(value)
            elif value.lower() in ["true", "false"]:
                user_data[key] = str_to_bool(value)
            else:
                user_data[key] = value
        
        all_users.append(user_data)

JSON_HEADER = {"data": all_users}

print("CONVERTED")

with open(JSON_URL, "w") as json_file:
    json.dump(JSON_HEADER, json_file, indent=4)

print("SAVED")
