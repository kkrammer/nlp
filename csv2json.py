#/usr/bin/python

import csv, json
import pandas as pandasForSortingCSV

#csvFilePath = "jlab-eda_20APR23.csv"
csvFilePath = "small.csv"
jsonFilePath = "emass.json"

#Read the csv and add the data to a dictionary

data = {}
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for csvRow in csvReader:
        cveid = csvRow["CVE ID"]
        data[cveid] = csvRow
        print(data)
        

#Write data to a root node.....
root={}
root["happy"] = data

#Write data to a json file
with open(jsonFilePath, "w") as jsonFile:
    jsonFile.write(json.dumps(root, indent=4))




