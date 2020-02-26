import csv

# in/out : brightness,acq_date,bright_t31,frp,state

source = 'Australian Capital Territory'
target = 'New South Wales'

dico = {}

with open(source + '.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
    
    for row in reader:
        date = row['acq_date']
        if (date in dico.keys()) :
            dico[date].append([row['brightness'], date, row['bright_t31'], row['frp'], target])
        else : 
            dico[date] = [[row['brightness'], date, row['bright_t31'], row['frp'], target]]


with open('merged.csv', 'w', newline='') as newcsvfile:
        writer = csv.writer(newcsvfile)
        writer.writerow(['brightness', 'acq_date', 'bright_t31', 'frp', 'state'])
        
        with open(target + '.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
            
            for row in reader:
                date = row['acq_date']
                if (date in dico.keys()):
                    for values in dico[date] :
                        writer.writerow(values)
                    del dico[date]
                writer.writerow([
                        row['brightness'], 
                        row['acq_date'], 
                        row['bright_t31'], 
                        row['frp'], 
                        row['state']
                        ])
                
                
                        
                

