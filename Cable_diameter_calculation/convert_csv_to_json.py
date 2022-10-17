import csv
import json


# defining the function to convert CSV file to JSON file
def convjson(csv_file, json_file):
    # creating a dictionary
    data = {}

    # reading the data from CSV file
    with open(csv_file, encoding='utf-8') as csvfile:
        csv_read = csv.DictReader(csvfile)

        # Converting rows into dictionary and adding it to data
        for rows in csv_read:
            key = rows['Провод']
            data[key] = rows

            # dumping the data
    with open(json_file, 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(json.dumps(data, indent=4))


csv_filename = r'C:\Python projects\cables\data\provoda_montazhnye.csv'
json_filename = r'C:\Python projects\cables\Cable_diameter_calculation\wires.json'

convjson(csv_filename, json_filename)
