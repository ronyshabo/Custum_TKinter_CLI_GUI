import sys
import requests
import json

from JSON_commands import *
from . import navigator, beorn_collector
from Zeus import *



############### Output functions
###### responsible to out put the results to it's textbox widnow
def output_to_junipor_textbox(self, output_entitiy):
    output = self.juni_output_textbox.insert("0.0", output_entitiy)
    return 
def output_to_address_textbox(self, output_entitiy):
    output = self.address_output_textbox.insert("0.0", output_entitiy)
    return
def output_to_rad_textbox(self, output_entitiy):
    output = self.rad_output_textbox.insert("0.0", output_entitiy)
    return
def output_to_adva_textbox(self, output_entitiy):
    output = self.adva_output_textbox.insert("0.0", output_entitiy)
    return



############## drop menu variables
######## Imports the Value of each drop menu
def drop_menu_variable(self):
    choice = self.main_command.get()
    return choice

def sub_menu_variable(self):
    sub_choice = self.Sub_command.get()
    return sub_choice

############### Text box cleaner
####### clears out all the windows after each use "using the Devices button"
def text_box_cleaner(self):
    self.juni_output_textbox.delete("0.0","end")
    self.address_output_textbox.delete("0.0","end")
    self.adva_output_textbox.delete("0.0","end")
    self.rad_output_textbox.delete("0.0","end")


def device_sorter(self):
    """
    Gets initialized after pressing the Devices button
    requires 3 arguments
    - CID
    - a main command
    - and a sub command
    collects the list of devices and their ip addresses 
    the decides which JSON file to use to inherit the correct command and sub-command 
    so far I have the list of ips visible on it's own textbox window. hoping to replace it with CISCO commands 
    and use the IPs to automatically sendf the commands to a session using SSH
    """
    devices_list = beorn_collector.beorn_api_caller(self)
    drop_menu_key= drop_menu_variable(self).lower()
    sub_menu_key = sub_menu_variable(self).lower()
    text_box_cleaner(self)

    ip_list =[]
    ips_dict = {}
    for device in devices_list:

        if device["vendor"]=="JUNIPER":
            juni_list=[]
            # self.juni_output_textbox.delete('1.0',self.END)
            juni_ip = device["IpAddress"]
            ips_dict = {"Junipor":juni_ip}
            ip_list.append(ips_dict)
            json_file = open("C:/Users/P3101630/Desktop/GUI CLI/JSON_commands/junipor.json","r")
            commands = json.load(json_file)
            key = commands[drop_menu_key][sub_menu_key]

            output_to_junipor_textbox(self,key)           
            

        if device["vendor"]=="RAD":
            rad_ip = device["IpAddress"]
            ips_dict = {"Rad":rad_ip}
            ip_list.append(ips_dict)
            json_file = open("C:/Users/P3101630/Desktop/GUI CLI/JSON_commands/rad.json","r")
            commands = json.load(json_file)
            key = commands[drop_menu_key]
            output_to_rad_textbox(self,key)
            

        if device["vendor"]=="ADVA":
            adva_ip = device["IpAddress"]
            ips_dict = {"ADVA":adva_ip}
            ip_list.append(ips_dict)
            json_file = open("C:/Users/P3101630/Desktop/GUI CLI/JSON_commands/adva.json","r")
            commands = json.load(json_file)
            key = commands[drop_menu_key]
            output_to_adva_textbox(self,key)
  
    output_to_address_textbox(self,devices_list)


def ssh_connection(self):
    """
    Still Under Construction 'Current stage : Planning'
    """
    return