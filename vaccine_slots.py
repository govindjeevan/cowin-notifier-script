#!/usr/bin/env python

IFTTT_KEY = ""
DISTRICT_ID = ""

headers = {
    'authority': 'cdn-api.co-vin.in',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'accept': 'application/json, text/plain, */*',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'origin': 'https://selfregistration.cowin.gov.in',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://selfregistration.cowin.gov.in/',
    'accept-language': 'en-US,en;q=0.9,cs;q=0.8',
}




import datetime
import requests
import os
from datetime import timedelta, date


def ifttt_alert(vaccine, slots, date, center):
    report = {}
    report["value1"] = str(vaccine)+" ("+str(slots)+")"
    report["value2"] = str(date)
    report["value3"] = str(center)
    if len(IFTTT_KEY) > 0:
        requests.post("https://maker.ifttt.com/trigger/vaccine_slot/with/key/"+IFTTT_KEY, data=report)
    
def write_csv(filename, line):
    should_write_header = os.path.exists(filename)
    with open(filename, 'a') as f:
        f.writelines(line+"\n")



def fetch_slots():
    write_csv("logs_vaccine.txt", timestamp)
    dates = [(date.today() + timedelta(days=i)).strftime("%d-%m-%Y") for i in range(5)]
    for day in dates:
        params = ( ('district_id', DISTRICT_ID), ('date', day) )
        response = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict', headers=headers, params=params)
        if response.ok:
            if len(response.json()['centers']) > 0:
                for center in response.json()['centers']:
                    for session in center['sessions']:
                        #write_csv("logs_vaccine.txt", str(center['name']) +" " + str(session['available_capacity']))
                        if str(session['date']) == day:
                            csv_row = ",".join([str(timestamp), str(center['center_id']), str(center['name']), str(session['date']), str(session['min_age_limit']), str(session['vaccine']), str(session['available_capacity'])])
                            ifttt_alert(session['vaccine'], session['available_capacity'], str(session['date']), str(center['name']))
                            write_csv("slot_data.csv", csv_row)
        else:
            write_csv("logs_vaccine.txt", "failed")

dates = [(date.today() + timedelta(days=i)).strftime("%d-%m-%Y") for i in range(5)]
timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S.%f")
fetch_slots()
