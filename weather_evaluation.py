import json

# ---PART 1---

# Open the JSON file and load it into a new variable
with open ('precipitation.json') as file:
    precipitation_data = json.load(file)

# Create the new (for now filled with 0's) list for the total monthly precipitation
monthly_precipitation = [0] * 12

# Find the measurements for Seattle per month and copy them into the list
for measurement in precipitation_data:
    if (measurement['station'] == 'GHCND:US1WAKG0038'):
        # Split the date string into a list of strings [year, month, day]
        date = measurement['date'].strip().split('-')
        # Uses the month (year is always 2010) to add to the month's position in the list the measured precipitation
        monthly_precipitation[int(date[1])-1] += measurement['value']

# Two new lists: one to contain the JSON output later and one for naming the months
    output = []
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# Make a new JSON file indicating the name of the month with the respective precipitation
with open('monthly_precipitation_seattle.json', 'w') as file:
    # Add a new dictionary to the list with the name and precipitation for each month
    for entry in monthly_precipitation:
        output.append({'month' : months[monthly_precipitation.index(entry)], 'value' : entry})
    # Write the output into the new JSON file
    json.dump(output, file, indent = 4)

# ---PART 2---

# Sum up the monthly precipitation to get the yearly total
precipitation_2010 = sum(monthly_precipitation)

# Create the new (for now empty) list for the relative monthly precipitation
monthly_precipitation_rel = []

# Calculate the relative to the annual precipitation for each month and add to the list
for entry in monthly_precipitation:
    monthly_precipitation_rel.append(float(entry / precipitation_2010))

# Print the resulting list on the screen
print(f'The annual precipitation in 2010 was {precipitation_2010} and for each month the relative amount was:')
for i in range(12):
    print(f'{months[i]}: {round(monthly_precipitation_rel[i], 2)}%')