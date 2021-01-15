import json

# Open the JSON file and load it into a new variable
with open ('precipitation.json') as file:
    precipitation = json.load(file)

# Create the new (for now empty) list for the total monthly precipitation
monthly_precipitation = [0] * 12
print(monthly_precipitation)

for entry in precipitation:
    if (entry['station'] == 'GHCND:US1WAKG0038'):
        # Split the date string into a list of strings [year, month, day]
        date = entry['date'].strip().split('-')
        # Uses the month (year is always 2010) to add to the month's position in the list the measured precipitation
        monthly_precipitation[int(date[1])-1] += entry['value']
print(monthly_precipitation)