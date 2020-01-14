import json

# open json data file
with open('precipitation.json', encoding='utf8') as file:
    dictionary_precipitation_data = json.load(file)

# defining the amount of months in the list to be formed
total_months = [0]*12

for measurement in dictionary_precipitation_data:
    # selecting the data collected in Seattle
    if measurement['station'] == 'GHCND:US1WAKG0038':
        # splitting the date to a separate year, month and day instead of one date value.
        (year, month, day) = measurement['date'].split('-')
        # the program detects the targeted month, it add the value to the current total for that month.
        total_months[int(month)-1] += measurement['value'] 
print(total_months)

# save the file as a json file.
with open('Part1_PassFail.json', 'w', encoding='utf8') as file:
    json.dump(total_months, file)

