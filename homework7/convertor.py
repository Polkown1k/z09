import json
import requests

url = 'http://www.nbrb.by/API/ExRates/Rates?Periodicity=0'

response = requests.get(url)
data = response.json()

rub_val = [data[16].get('Cur_Abbreviation'), data[16].get('Cur_OfficialRate')]
usd_val = [data[4].get('Cur_Abbreviation'), data[4].get('Cur_OfficialRate')]
eur_val = [data[5].get('Cur_Abbreviation'), data[5].get('Cur_OfficialRate')]

def rub_to_byn(value):
    value = value * (rub_val[1]/100)
    print ("%.2f" %value)

def usd_to_byn(value):
    value = value * (usd_val[1])
    print ("%.2f" %value)
    
def eur_to_byn(value):
    value = value * (eur_val[1])
    print ("%.2f" %value)

def byn_to_rub(value):
    value = value / (rub_val[1]/100)
    print ("%.2f" %value)

def byn_to_usd(value):
    value = value / (usd_val[1])
    print ("%.2f" %value)
    
def byn_to_eur(value):
    value = value / (eur_val[1])
    print ("%.2f" %value)    

byn_to_eur(13)
