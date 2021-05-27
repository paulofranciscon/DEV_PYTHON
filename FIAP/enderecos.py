from copy import copy

from pygeocoder import Geocoder

endereco = (input('Digite o endereço: '))
resultado = Geocoder('key API').geocode(endereco)
coordinates = Geocoder('key API').geocode(endereco).coordinates
                                                                #Access reverse to coordinates
#coordinates2 = Geocoder('AIzaSyDsF6-ETfWjCOTIxbwc6cnINqx8MNAeJho').reverse_geocode (-22.1984674, -49.9564299)

print(resultado)
print('Coordenadas: {}'.format(coordinates))
#print('Captura das Coordenadas: {}'.format(coordinates2))
