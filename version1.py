__author__ = 'aus'

import facebook
import re


#mesaave
mesa_ave_id = "621422037868632"
#tarifamesaalicantemadridalicante
tarifa_mesa_alc_mad_alc_id = "256075921093789"
#https://www.facebook.com/groups/512002085573921/
ave_alc_mad_alc_id = "512002085573921"


access_token = "CAACEdEose0cBAFI6ll267OFJhCyc2kjbZCtBzoL681Ieo6LC9F5K5o9EhlF1c7C0EdKFDuJfzQ4jUvUEZCtHKUaeZA3oHywcsr0x7y6TB02bsf3ynzZBRlupwDogefp21LVstadh3w9NAXOSND1sORN2GEGjrQAFtfz2sQ1aEb07kNnFQvrY8HKpnOqeIenCwOLQKu0fiwZDZD"
version = "2.4"

graph = facebook.GraphAPI(access_token, version)
graph.timeout = 100

# Get all the comments from a post

connection_name = 'feed'
feed = graph.get_connections(mesa_ave_id, connection_name)
feed_data = feed['data']
# Ejemplo del post 0 del feed
# post0 = feed_data[0]
# print post0['message']


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

#Mostrar todos los mensajes  del feed
feed_len = len(feed_data)
print "Feed lenght is " + str(feed_len)

for i in range(0, (feed_len)):

    mensaje = feed_data[i]['message']
    if (alc_mad_filter_search(mensaje) == True) and (date_filter_search(mensaje) == True):
        print "-----------------------------------"
        print "ID: " + feed_data[i]['id']
        print "Created time :" + feed_data[i]['created_time']
        print "MENSAJE = " + mensaje
        print "MATCHER = TRUE"
        print "-----------------------------------"

    # else:
    #     print "MENSAJE = " + mensaje
    #     print "MATCHER = FALSE"
    #     print "-------------------------------------------"



