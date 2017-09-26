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
print("\n Bus Line : ",lineref)
url="http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="+mtakey+"&VehicleMonitoringDetailLevel=calls&LineRef="+lineref

#url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="+ os.getenv("MTA_KEY")+"&VehicleMon\                        
#itoringDetailLevel=calls&LineRef=B52"                                                                                            

#downloading data                                                                                                                 
#req = urllib.request.urlretrieve(url,rawdata)                                                                                    
#unpacking into $PUIDATA                                                                                                          

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)
numberofbus = np.size(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])
print("\n Number of Active Buses :",numberofbus)
for i in range(numberofbus):
    latitude = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['\
VehicleLocation']['Latitude']
    longitude = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney'][\
'VehicleLocation']['Longitude']
    print("\n Bus {} is at latitude {} and longitude {}".format(i, latitude, longitude))
