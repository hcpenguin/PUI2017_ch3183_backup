from __future__ import print_function
import os
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
import sys
import numpy as np

mtakey = sys.argv[1]
lineref = sys.argv[2]
bus_info = sys.argv[3]

url="http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="+mtakey+"&VehicleMonitoringDetailLevel=calls&LineRef="+lineref
#url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="+ os.getenv("MTA_KEY")+"&VehicleMon\
#itoringDetailLevel=calls&LineRef=B52" 


#load json file and data
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

#businfo
businfo = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

#open CSV file and write
fout = open(bus_info, "w")
fout.write("Latitude, Longitude, Stop Name, Stop Status\n")
for i in range(len(businfo)):
    latitude = businfo[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    longitude = businfo[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    #if no information in OnwardCalls,stop info is N/A
    if businfo[i]['MonitoredVehicleJourney']['OnwardCalls']!={}:
        stop_name = businfo[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
        stop_status = businfo[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
    else:
        stop_name = stop_status = "N/A" 
    fout.write(str(latitude))
    fout.write(",")
    fout.write(str(longitude))
    fout.write(",")
    fout.write(stop_name)
    fout.write(",")
    fout.write(stop_status)
    fout.write("\n")
fout.close()
