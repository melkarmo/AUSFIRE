import csv

# in/out : brightness,acq_date,bright_t31,frp,state

states = [
            'Queensland',
            'Victoria',
            'New South Wales',
            'South Australia',
            'Tasmania',
            'Northern Territory',
            'Western Australia',
            'Australian Capital Territory'
        ]

for state in states: 

    with open('new_fire_dataset.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
        
        with open('grouped/' + state + '.csv', 'w', newline='') as newcsvfile:
            writer = csv.writer(newcsvfile)
            writer.writerow(['brightness', 'acq_date', 'bright_t31', 'frp', 'state'])
        
            for row in reader:
                if (row['state'] == state):
                    writer.writerow([
                            row['brightness'], 
                            row['acq_date'], 
                            row['bright_t31'], 
                            row['frp'], 
                            row['state']
                            ])

