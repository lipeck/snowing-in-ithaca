import csv

day = "-03-29"
last = 0
lastsnow = 0
blizzard = ''
maxsnowfall = 0

with open('../snowfall.csv', 'r') as f:
    reader = csv.DictReader(f)
    
    for row in reader:
        date = row['DATE']
        #convert snowfall values to integers
        snow = int(float(row['SNOW']))

        if day in date:
            if snow > maxsnowfall:
                maxsnowfall = snow
                blizzard = date
                print(maxsnowfall, date)
        else: continue
    
        if day in date and snow >= 0.5:
            
            if last < int(date[:4]):
                last = int(date[:4])
                lastsnow = snow
        else: continue

if last == 0: exit()
            
if last == int(blizzard[:4]):
    print(f"the last time it snowed in Ithaca on {day}, it snowed {lastsnow}' in {last}! that is the most it has ever snowed on {day}!")

if last != int(blizzard[:4]) and lastsnow > 0 and maxsnowfall > 0:
    print(f"the last time it snowed in Ithaca on {day}, it snowed {lastsnow}' in {last}! the most it has ever snowed on {day} is {maxsnowfall}' in {blizzard[:4]}!")

# if last 

print(last, lastsnow)
    
print(blizzard, maxsnowfall)

#prints snowfall level
        # prints years with snowfall data
        # if day in date and snow >= 0.5:
        #     print(row['DATE'], row['SNOW'])