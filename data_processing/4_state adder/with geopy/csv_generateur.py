import csv
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="ausfire_dataviz_moncef", timeout=None)

def cut_ends(chaine):
    return chaine[1:-1]
        
def get_state(lati, longi):
    lat, long = cut_ends(lati), cut_ends(longi)
    location = geolocator.reverse(lat + ', ' + long)
    try:
        res = location.raw['address']['state']
        return res
    except:
        return 'New South Wales'
    
nb_lines = 0

with open('new_fire_dataset.csv') as f:
    nb_lines = sum(1 for line in f)
        
with open('new_fire_dataset.csv', 'a', newline='') as newcsvfile:
    writer = csv.writer(newcsvfile)
    with open('fire_dataset_cleaned.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
        if (nb_lines == 0) :
            writer.writerow(['state', 'brightness', 'acq_date', 'bright_t31', 'frp'])
            nb_lines += 1
        compteur = 1
        for row in reader:
            if (compteur < nb_lines) :
                compteur += 1
            else :
                state = get_state(row['"latitude"'], row['"longitude"'])
                writer.writerow([state, 
                                 cut_ends(row['"brightness"']), 
                                 cut_ends(row['"acq_date"']), 
                                 cut_ends(row['"bright_t31"']), 
                                 cut_ends(row['"frp"'])
                                 ])
                    
