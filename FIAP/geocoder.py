#https://geocoder.readthedocs.io/

from pygeocoder import Geocoder

endereco = '141, Amélia Carraro Pavão, Piracicaba,SP'

print(Geocoder('AIzaSyDsF6-ETfWjCOTIxbwc6cnINqx8MNAeJho').geocode(endereco).coordinates)