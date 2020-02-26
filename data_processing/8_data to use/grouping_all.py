import csv

# in/out : acq_date,count,max_brightness,max_bright_t31,max_frp,state,fire_area

states = [
            'Queensland',
            'Victoria',
            'New South Wales',
            'South Australia',
            'Tasmania',
            'Northern Territory',
            'Western Australia',
        ]

with open('fire_dataset.csv', 'w', newline='') as newcsvfile:
            writer = csv.writer(newcsvfile)
            writer.writerow(['acq_date','count','max_brightness','max_bright_t31','max_frp','state','fire_area'])
            
            for state in states: 

                with open('bystate/' + state + '.csv', newline='') as csvfile:
                    reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
                    
                    for row in reader:
                        writer.writerow([
                                row['acq_date'], 
                                row['count'], 
                                row['max_brightness'], 
                                row['max_bright_t31'], 
                                row['max_frp'],
                                row['state'], 
                                row['fire_area']
                                ])