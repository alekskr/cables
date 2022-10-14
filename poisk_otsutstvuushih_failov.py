import os
import json

all_files_cable_types = os.listdir('all_diameters_provoda_montazhnye_s_kombinirovannoy_izolyatsiey')
del all_files_cable_types[0]
print(all_files_cable_types)

with open('all_diameters_provoda_montazhnye_s_kombinirovannoy_izolyatsiey\\all_diameters.json', encoding='UTF-8') as file:
    all_cable_diameters = json.load(file)

propusk = {}
for k, v in all_cable_diameters.items():
    k_file = k + '.html'
    if k_file not in all_files_cable_types:
        propusk[k_file] = v

print(propusk)

with open('all_diameters_provoda_montazhnye_s_kombinirovannoy_izolyatsiey\\propusk.json', 'w', encoding='UTF-8') as file:
    json.dump(propusk, file, indent=4, ensure_ascii=False)
