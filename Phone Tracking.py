import phonenumbers
import requests
from phonenumbers import geocoder, carrier
phone_number1 = phonenumbers.parse("+91")
print(geocoder.description_for_number(phone_number1, "en"))

print(carrier.name_for_number(phone_number1, 'en'))





############################################################  End Program   ##############################################################################################
