
from xml.dom import minidom
import xml.etree.ElementTree as ET

tree = ET.parse('wsj_0010_sample.txt.se.xml')
root = tree.getroot()

# Dict of dict to be able to store data
data = {'Organization.ORGANIZATION' : {},
'Person.PERSON' : {},
'Location.LOCATION' : {}}

nbValues = 0;
# Iterate through every entity
for specific_entity in root.iter('specific_entity'):
    nbValues = nbValues + 1;
    type = specific_entity.find('type').text;
    # Checking if named entity
    if type=="Organization.ORGANIZATION" or   type=="Person.PERSON" or type=="Location.LOCATION":
        name = specific_entity.find('string').text
        # Does it exist
        if name in data[type]:
            data[type][name] = data[type][name] + 1;
        else:
            data[name] = 1;
            data[type][name] = 1;

#Print of the named entities
#nbValues = len(data["Organization.ORGANIZATION"].keys()) + len(data["Person.PERSON"].keys()) + len(data["Location.LOCATION"].keys()) #total number of named entities
print('Entité nommée                Type                Nb occ                Proportion(%)')
for type in ["Organization.ORGANIZATION", "Person.PERSON", "Location.LOCATION"]:
    for name in data[type] :
        print(name+"                "+type+"                "+str(data[type][name])+"                "+str((int(data[type][name])*100)/nbValues)  )
        print(data[type][name])
