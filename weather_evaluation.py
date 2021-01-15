import json

# Open the JSON file and load it into a new variable
with open ('precipitation.json') as file:
    precipitation_data = json.load(file)

# Create the new (for now empty) list for the total monthly precipitation
monthly_precipitation = [0] * 12

# Find the measurements for Seattle per month and copy them into the list
for measurement in precipitation_data:
    if (measurement['station'] == 'GHCND:US1WAKG0038'):
        # Split the date string into a list of strings [year, month, day]
        date = measurement['date'].strip().split('-')
        # Uses the month (year is always 2010) to add to the month's position in the list the measured precipitation
        monthly_precipitation[int(date[1])-1] += measurement['value']

# Make a new JSON file indicating the name of the month with the respective precipitation
with open('monthly_precipitation_seattle.json', 'w') as file:
    output = []
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    for entry in monthly_precipitation:
        output.append({'month' : months[monthly_precipitation.index(entry)], 'value' : entry})
    json.dump(output, file, indent = 4)