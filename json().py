# ************  json()

"""     
		Python JSON is a format for structuring data. 
  It is mainly used for storing and transferring data between 
  the browser and the server. Python too supports JSON with a 
  built-in package called JSON. This package provides all 
  the necessary tools for working with JSON Objects including 
  parsing, serializing, deserializing, and many more. 
        
"""

# ********** simple json() in use
# ********** json.loads(jsonObj) converts JSON to python dictionary
# ********** json.dumps(pythonDict) converts python dict to json object

import json

data = '{"name":"Fiji", "country":"japan"}'
# print(data)								
# output
# # {"name":"Fiji", "country":"japan"}

convertedToDict=json.loads(data) # converts json object to dictionary
# print(convertedToDict)					
# output
# {'name': 'Fiji', 'country': 'japan'}

# print(convertedToDict["name"])			
# output
# Fiji

convertedToJson=json.dumps(convertedToDict) # converts dictionary to Json object
# output
# {"name": "Fiji", "country": "japan"}

convertedToJson=json.dumps(convertedToDict, indent=4) 

# print(convertedToJson)
# output
# {
#     "name": "Fiji",
#     "country": "japan"
# }

# How python and JSON data types differs?, the following example shows

profile = {
	"name" : "Mahdi",
	"age" : 25,
	"country" : "Australia",
	"uni" : "Jipmer",
	"degree" : True,
	"skills" : ("Vascular", "Neurosurgical"),
	"experience" : 1.5,
	"driving" : None, 
	"crime_record" : "", 
}

# print(profile)

convertedToJson= json.dumps(profile, indent=2)
# print(convertedToJson)

# output
# {
#   "name": "Mahdi",
#   "age": 25,
#   "country": "Australia",
#   "uni": "Jipmer",
#   "degree": true,
#   "skills": [
#     "Vascular",
#     "Neurosurgical"
#   ],
#   "experience": 1.5,
#   "driving": ""
# }

# Iterating over dictionary
for key in profile:
  print(key," : ",profile[key]);
  
# output
# name  :  Mahdi
# age  :  25
# country  :  Australia
# uni  :  Jipmer
# degree  :  True
# skills  :  ('Vascular', 'Neurosurgical')
# experience  :  1.5
# driving  :  None
# crime_record  :


# dictionary to be dumped 
  
with open('myfile.json', 'w', encoding ='utf8') as json_file: 
    json.dump(profile, json_file, allow_nan=True, indent=5) 

# allow_nan set to True, the error will not be generated