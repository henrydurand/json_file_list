import os
import json

directory = input('Input file directory: ')
file_list = os.listdir(directory)

sorted_file_list = sorted(file_list)

output_file = 'sorted_files.json'

with open(output_file, 'w') as f:
    json.dump(sorted_file_list, f, indent=4)

print('JSON list exported!')