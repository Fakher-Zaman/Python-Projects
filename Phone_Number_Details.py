# $ pip install phonenumbers

import phonenumbers
from phonenumbers import timezone, geocoder, carrier

number = input("Enter Your Phone Number Here With +92: ")
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
carr = carrier.name_for_number(phone, "en")
reg = geocoder.description_for_number(phone, "en")
print(phone)
print(time)
print(carr)
print(reg)