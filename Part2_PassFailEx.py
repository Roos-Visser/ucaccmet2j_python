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

total_year = sum(total_months)

# defining the amount of months in the list to be formed
percentage = [0]*12
# calculate relative precipitation per month compared to the total precipitation over the whole year in percentages.
for month in range(12):
    percentage[month] = total_months[month] / total_year * 100
print(percentage)

dictionary_seattle = {
	"Seattle": {
		"station": "GHCND:US1WAKG0038", 
		"state": "WA", 
		"totalMonthlyPrecipitation": total_months, 
		"relativeMonthlyPrecipitation": percentage, 
		"totalYearlyPrecipitation": total_year,
	}
}

# save the file as a json file.
with open('Part2_PassFail.json', 'w', encoding='utf8') as file:
    json.dump(dictionary_seattle, file)

