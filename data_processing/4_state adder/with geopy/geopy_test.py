# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 16:18:24 2020

@author: melkarmo
"""

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="specify_your_app_name_here")
location = geolocator.reverse("-41.501960, 147.272468")
print(location.address)
#Potsdamer Platz, Mitte, Berlin, 10117, Deutschland, European Union
print((location.latitude, location.longitude))
#(52.5094982, 13.3765983)
print(location.raw['address']['state'])
#{'place_id': '654513', 'osm_type': 'node', ...}


"""
from geopy.exc import GeocoderTimedOut
def do_geocode(lati, longi):
    try:
        return geopy.geocode(address)
    except GeocoderTimedOut:
        return do_geocode(address)"""

"""def get_state(lati, longi):
    lat, long = cut_ends(lati), cut_ends(longi)
    try:
        location = geolocator.reverse(lat + ', ' + long)
        try:
            res = location.raw['address']['state']
            return res
        except:
            return 'New South Wales'
    except GeocoderTimedOut:
        return get_state(lati, longi)"""

    
#"latitude","longitude","brightness","acq_date","bright_t31","frp"