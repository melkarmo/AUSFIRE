import csv

# in : brightness,acq_date,bright_t31,frp,state
# out : acq_date, count, max_brightness, max_bright_t31, max_frp, state

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

    dico = {}
    
    with open('grouped/' + state + '.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
        
        for row in reader:
            if (row['acq_date'] in dico.keys()) :
                dico[row['acq_date']][0] += 1
                dico[row['acq_date']][1] = max(dico[row['acq_date']][1], float(row['brightness']))
                dico[row['acq_date']][2] = max(dico[row['acq_date']][2], float(row['bright_t31']))
                dico[row['acq_date']][3] = max(dico[row['acq_date']][3], float(row['frp']))
            else : 
                dico[row['acq_date']] = [
                        1, 
                        float(row['brightness']), 
                        float(row['bright_t31']), 
                        float(row['frp'])
                        ]
        
    with open('reduced/' + state + '_reduce.csv', 'w', newline='') as newcsvfile:
        writer = csv.writer(newcsvfile)
        writer.writerow(['acq_date', 'count', 'max_brightness', 'max_bright_t31', 'max_frp', 'state'])
    
        for key in dico.keys() :
            writer.writerow([
                    key, 
                    dico[key][0], 
                    int(dico[key][1] - 273.15), 
                    int(dico[key][2] - 273.15), 
                    dico[key][3], 
                    state
                    ])

