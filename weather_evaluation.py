import json

# A list of month names that will be used for all parts
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# ---PART 1/3---

# Open the JSON file and load it into a new variable
with open ('precipitation.json') as file:
    precipitation_data = json.load(file)

# Open the CSV file and find the station codes
with open ('stations.csv') as file:
    # Read the headings and save to a variable as list of strings
    headings = file.readline().strip().split(',')
    # New list of dictionaries with station name and sation code
    # Changes to the CSV file that don't change column names or remove them don't affect this code
    station_info = []
    for line in file:
        line = line.strip().split(',')
        station_info.append({'city': line[headings.index('Location')], 'station': line[headings.index('Station')]})
print(station_info)

# Repeat this process for each city in which precipitation was measured
for city in station_info:
    print(f'Working on {city["city"]}')
    # CALCULATIONS
    # Create the new (for now filled with 0's) list for the total monthly precipitation
    monthly_precipitation = [0] * 12
    # Find the city's entries in the original JSON and transfer their sum to the list
    for measurement in precipitation_data:
        if (measurement['station'] == city['station']):
            # Split the date string into a list of strings [year, month, day] = postions 0, 1, 2
            date = measurement['date'].strip().split('-')
            # Uses position 2 to determine the month and adds the value to the convenient position in the list
            monthly_precipitation[int(date[1])-1] += measurement['value']
    
    # OUTPUT INTO NEW JSON's
    output = []
    # Make a new JSON file for each city indicating the name of the month with the respective precipitation
    with open(f'monthly_precipitation_{city["city"]}.json', 'w') as file:
        # Adding a counting variable to go through from 0 to 12
        count = 0
        # Add a new dictionary to the list with the name (months list) and precipitation for each month (entry)
        for entry in monthly_precipitation:
            output.append({'month' : months[count], 'value' : entry})
            count += 1
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
    print(f'The annual precipitation in {city["city"]} in 2010 was {precipitation_2010} and for each month the relative amount was:')
    for i in range(12):
        print(f'{months[i]}: {round(monthly_precipitation_rel[i], 3) * 100}%')
    print()