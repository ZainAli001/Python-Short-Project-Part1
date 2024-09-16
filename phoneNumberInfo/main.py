import phonenumbers
from opencage.geocoder import OpenCageGeocode
from phonenumbers import timezone, carrier, geocoder
import folium
from prettytable import PrettyTable
x = PrettyTable(padding_width=5)


print("\t\t\t-------------------------------------")
print()
print("\t\t\t*********** Phone Locator ***********")
print()
print("\t\t\t-------------------------------------")
number = input("Enter Number here : ")


phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
location = geocoder.description_for_number(phone, "en")
simNetwork = carrier.name_for_number(phone, "en")

x.field_names = ["Phone number ", "Country Code",
                 "City", "location", "SIM Network"]
x.add_row([number, phone, time[-1], location, simNetwork])
print(x)


key = "8c1d3446946e49c2afc42b0394f4fc0d"
geocoder = OpenCageGeocode(key)
query = str(location)
result = geocoder.geocode(query)


lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
# print(lat, lng)


myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save("mylocation.html")
