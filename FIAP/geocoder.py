#https://geocoder.readthedocs.io/

from pygeocoder import Geocoder

endereco = 'Digite o Endereço'

print(Geocoder('Key API GOOGLE').geocode(endereco).coordinates)
