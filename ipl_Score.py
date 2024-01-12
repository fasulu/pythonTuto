# ************  Getting IPL cricket score

"""     
		A simple api request to show IPL cricket scores
        Show desktop notification every 10 seconds and 
        hide after 5 seconds
        
"""

# ****************** 

import requests
from win10toast import ToastNotifier
from time import sleep
import xml.etree.ElementTree as ET

url = "http://static.cricinfo.com/rss/livescores.xml"

def sendNotification(title, message):
    obj=ToastNotifier()
    obj.show_toast(title, message, icon_path="None", duration=5)

while True:
    req=requests.get(url)
    data=req.text
    # print(data)
    xml_Data = ET.fromstring(data)
    channel=xml_Data.find('channel')
    for item in channel.findall('item'):
        title=item.find('title')
        if 'Mumbai' in title.text:
            sendNotification("IPL Score", title.text)
    sleep(10)
        