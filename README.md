# COWIN VACCINE AVAILABILITY NOTIFICATION - Self Host

## Setting up IFTTT Notifications

1. https://ifttt.com/create
2. Add If This
3. Search and click "Webhooks"
4. Set Event Name as vaccine_slot
5. Create Trigger
6. Add Then That
7. Notifications
8. Send Notifications to IFTTT app (Download from PlayStore)
9. Paste below text in Message field
   {{EventName}}: {{Value1}} - {{Value2}} - {{Value3}}
10. Create Action
11. Continue
12. Finish
13. Go here https://ifttt.com/maker_webhooks/settings
14. Find a URL: https://maker.ifttt.com/use/{API_KEY}
15. Copy the API_KEY section from the URL
16. Set IFTTT_KEY with API_KEY value in vaccine_slots.py script


## Running the script repeatedly

### Windows
Won't provide walkthrough, but entirely doable with some googling
https://dev.to/tharindadilshan/running-a-python-script-every-x-minutes-in-windows-10-3nm9

### Linux
1. crontab -e
2. Paste below command in the file that opens ( 5 => Ping cowin every 5 minute, change to desired interval )
  */1 * * * * /home/pi/vaccine_slots.py


A python script to notify you via IFTTT app whenever a slot becomes available at https://www.cowin.gov.in/
