import csv
import time
import reverse_geocoder as rg

def to_float(chaine):
    return float(chaine[1:-1])

def cut_ends(chaine):
    return chaine[1:-1]
    
start = time.time()

coordinates = []
lines = []
        
with open('fire_dataset_cleaned.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        lati = to_float(row['"latitude"'])
        long = to_float(row['"longitude"'])
        coordinates.append((lati,long))
        data = [
                cut_ends(row['"brightness"']), 
                cut_ends(row['"acq_date"']), 
                cut_ends(row['"bright_t31"']), 
                cut_ends(row['"frp"'])
                ]
        lines.append(data)
        
results = rg.search(coordinates, mode=1)
i = 0
for result in results:
    lines[i].append(result['admin1'])
    i += 1
    
with open('new_fire_dataset.csv', 'w', newline='') as newcsvfile:
    writer = csv.writer(newcsvfile)
    writer.writerow(['brightness', 'acq_date', 'bright_t31', 'frp', 'state'])
    for line in lines :
        writer.writerow(line)
    
end = time.time()

print(end-start)