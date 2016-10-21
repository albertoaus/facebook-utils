__author__ = 'aus'

import re
import json

def mad_alc_filter_search(mensaje):
    """Filtro para trayectos de Madrid a Alicante"""
    is_valid = False

    pattern_trip = "(mad.{1,}al)"   # Pilla  Alguien o Al como Alicante

    matcher_trip = re.search(pattern_trip, mensaje, re.IGNORECASE)

    if matcher_trip != None:
        is_valid = True

    return is_valid

def alc_mad_filter_search(mensaje):
    """Filtro para trayectos de Alicante a Madrid"""
    is_valid = False
    #Separadores: Que empice por alicante y termine por Madrid
    #filter = refindall('Alicante')
    #matcher = filter.search(mensaje)
    #print "MATCHER: " + str(matcher)

    alicante = ['ALC', 'ALIC', 'ALI', 'ALICANTE']
    separador = [' ',  ' a ', ' -', '- ', ' - ', ' /', '/ ', ' / ']
    madrid = ['MAD', 'MADRID']
    #Tengo que tener varios patterns e ir mejorandolos   --> Alicante- Madrid
    pattern_trip = "(al.{1,}mad)"   # Pilla  Alguien o Al como Alicante

    matcher_trip = re.search(pattern_trip, mensaje, re.IGNORECASE)

    if matcher_trip != None:
        is_valid = True

    return is_valid

def date_filter_search(mensaje):
    is_valid = False
    dia = 17
    month = "septiembre" # Cuidado con el mes porque a veces la gente no lo pone
    pattern_day = "( " + str(dia) + " )"
    matcher_date = re.search(pattern_day, mensaje, re.IGNORECASE)

    if matcher_date != None:
        is_valid = True

    return is_valid

with open('test.json') as data_file:
    json_input = json.load(data_file)

json_len = len(json_input)
filtered_list = []

for i in range(0, (json_len)):

    message = json_input[i]['message']
    #if (alc_mad_filter_search(message) == True) and (date_filter_search(message) == True):
    filtered_list.append(json_input[i])


# Save the Json into a file
with open('filter_test.json', 'w') as outfile:
    json.dump(filtered_list, outfile)
