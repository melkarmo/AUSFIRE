import csv
from math import pi

# in : acq_date,count,max_brightness,max_bright_t31,max_frp,state
# out : acq_date,count,max_brightness,max_bright_t31,max_frp,state,fire_area

def get_fire_area(count):
    return round(pi*0.5*0.5*count, 2)

states = [
            'Queensland',
            'Victoria',
            'New South Wales',
            'South Australia',
            'Tasmania',
            'Northern Territory',
            'Western Australia'
        ]

for state in states: 

    with open('reduced/' + state + '_reduce.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
        
        with open('reduced_with_fire/' + state + '.csv', 'w', newline='') as newcsvfile:
            writer = csv.writer(newcsvfile)
            writer.writerow(['acq_date','count','max_brightness','max_bright_t31','max_frp','state','fire_area'])
        
            for row in reader:
                writer.writerow([
                        row['acq_date'], 
                        row['count'], 
                        row['max_brightness'], 
                        row['max_bright_t31'], 
                        row['max_frp'], 
                        row['state'], 
                        get_fire_area(int(row['count']))
                        ])

