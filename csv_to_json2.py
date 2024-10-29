import csv
import json

JSON_HEADER = {
    "version": 2,
    "data": {
        "api::centro-trabajo.centro-trabajo": {}
    }
}

with open(CSV_URL, mode="r") as csvfile:
    reader = csv.DictReader(csvfile)
    
    count = 0
    
    for row in reader:
        count = count + 1
        
        id_key = str(count)
        
        JSON_HEADER["data"]["api::centro-trabajo.centro-trabajo"][id_key] = {
            key: (int(value) if value.isdigit() else value)
            for key, value in row.items()
        }

with open(JSON_URL, "w") as json_file:
    json.dump(JSON_HEADER, json_file, indent=4)