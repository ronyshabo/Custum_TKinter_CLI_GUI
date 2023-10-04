import sys
import requests


sys.path.insert(0, "GUI CLI\Zeus.py")
sys.path.insert(0, "GUI CLI\scripts.navigator.py")


import logging
from . import navigator



logging.basicConfig(
    filename="./logs/Zeus.log",
    level=logging.DEBUG,
    format="%(module)s : %(levelname)s:  %(message)s - : %(asctime)s",
)

def output_to_junipor_textbox(self, output_entitiy):
    output = self.juni_output_textbox.insert("0.0", output_entitiy)
    return 

def beron_call(self):
    CID = self.CID_Entry.get()
    beorn_get_link = "https://sense.chtrse.com/beorn/v3/topologies?cid="
    #TODO CID needs a clean up from all spaces
    CID = self.CID_Entry.get()
    full_link = beorn_get_link + str(CID)
    r = requests.get(full_link)
    data = r.json()
    return data


list_of_dicts=[]
is_multi = False


def multi_leg_decider(self):
    """
    This function looks at the topologies from beorn and decides if the circuit is Multi legged or not
    By looking at the first key value of the dictionary. 
    """
    is_multi = False
    CID = self.CID_Entry.get()
    data = beron_call(self)
    for checker in data:
        break
    if checker == 'customerName':
        is_multi = False
    if checker == 'PRIMARY':
        is_multi = True
    else:
        output_to_junipor_textbox(self,f"BEORN - Granite Call - No records in Granite found for{CID}")

    return is_multi



def beorn_api_caller(self):
    """
    Beorn API Caller
    the return is the combination of the vendor, and the Ip address fro each and every device

    [{'vendor': 'JUNIPER', 'IpAddress': '000.000.000.000'}.....]

    the Idea behind the Ip address , future plans includs using it to log into the device itself in a new 
    shell prompt and apply the command from JSOn file that matches the vendor
    """
    list_of_dicts = []

    data = beron_call(self)
    is_multi = multi_leg_decider(self)

    if is_multi == False: 
        topologies = data['topology']
        for topo in topologies:
            for node in topo['data']['node']:
                device_dict = {}  # Create a new dictionary for each device
                for item in node['name']:
                    if item["name"] == "vendor":
                        device_dict["vendor"] = item["value"]
                    if item["name"] == "managementIP":
                        device_dict["IpAddress"] = item["value"]
                list_of_dicts.append(device_dict)
    
    if is_multi == True:
        topologies = data['PRIMARY']['topology']
        for topo in topologies:
            for node in topo['data']['node']:
                device_dict = {}  # Create a new dictionary for each device
                for item in node['name']:
                    if item["name"] == "vendor":
                        device_dict["vendor"] = item["value"]
                    if item["name"] == "managementIP":
                        device_dict["IpAddress"] = item["value"]
                list_of_dicts.append(device_dict)

    return list_of_dicts
    

