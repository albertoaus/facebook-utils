__author__ = 'aus'
import os
from pprint import pprint
import json

#Script to analise the last messages of a facebook group

#Get the data of a group

#mesaave
mesa_ave_id = "621422037868632"
#tarifamesaalicantemadridalicante
tarifa_mesa_alc_mad_alc_id = "256075921093789"
#https://www.facebook.com/groups/512002085573921/
ave_alc_mad_alc_id = "512002085573921"

##os.system('python data_recolector.py ' + mesa_ave_id )
#Run the filter'
os.system('python filter.py')

#Print results
with open('filter_test.json') as data_file:
    pprint(json.load(data_file))