#!/usr/bin/python 

import subprocess

def getMPC():
    output = subprocess.Popen("mpc", stdout=subprocess.PIPE).stdout.read()
    tokens = output.split("\n")

    if ("[playing]" in output):
        return tokens[0] + " | " + tokens[1].split()[1] + " | " + tokens[1].split()[2]
    else:
        return "N/A"

def getT():
    return "T=" + open("/proc/acpi/ibm/thermal").read().split()[1] + "C"

def getDate():
       return subprocess.Popen("date", stdout=subprocess.PIPE).stdout.read()


print getMPC() + " | " + getT() + " | " + getDate()
