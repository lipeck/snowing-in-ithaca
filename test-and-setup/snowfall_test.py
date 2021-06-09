import csv

with open('../snowfall.csv', 'r') as f:
    reader = csv.DictReader(f)
    
    dates = []
    snowamt = []

    for row in reader:
        date = row['DATE']
        snow = int(float(row['SNOW']))

        dates.append(date)
        snowamt.append(snow)

        if snow > 16:
            print(row['DATE'], row['SNOW'])