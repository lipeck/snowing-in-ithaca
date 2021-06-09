import csv

last_year_day = "-02-01"

with open('../snowfall.csv', 'r') as f:
    reader = csv.DictReader(f)
    
    dates = []
    snowamt = []

    for row in reader:
        date = row['DATE']
        #convert snowfall values to integers
        snow = int(float(row['SNOW']))

        dates.append(date)
        snowamt.append(snow)

#prints snowfall level
        # if snow > 16:
        #     print(row['DATE'], row['SNOW'])

        # prints years with snowfall data
        if last_year_day in date and snow >= 0.5:
            print(row['DATE'], row['SNOW'])