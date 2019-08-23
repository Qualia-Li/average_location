from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="Average Location")
berkeley = geolocator.geocode("Berkeley, CA")
sf = geolocator.geocode("San Francisco, CA")
pa = geolocator.geocode("Palo Alto, CA")
sm = geolocator.geocode("San Mateo, CA")
sj = geolocator.geocode("San Jose, CA")
cities = [berkeley, sf, pa, sm, sj, sj, sj, sj]
average_longitude = sum(city.longitude for city in cities) / len(cities)
average_latitude = sum(city.latitude for city in cities) / len(cities)
place = (average_latitude, average_longitude)
print(place)
print(geolocator.reverse(place))
