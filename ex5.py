import json
import os

#path
ex5 = os.getcwd()
#reading json file
json_ex5_file_path = '%s %s' % (ex5, 'ex5.json')

#dict
ex5_properties = {}

#open json
try:
    with open(r'C:\Users\sival\Desktop\json\ex5.json') as f:
        ex5_properties = json.load(f)

except IOError as e:
    print (e)
    print ('IOError: Unable to open ex5.json. Terminating execution')
    exit(1)

print (ex5_properties)

for i in ex5_properties:
    
    if i['name'] == 'Old Fashioned':
        x=i['batters']['batter']
        
        max_id=0
        for id in x:
            cur_id = int(id["id"])
            if cur_id > max_id:
                max_id = cur_id
        last_id=str(max_id + 1)
        z={ "id": last_id, "type": "Coffee" }
        x.append(z)

with open(r'C:\Users\sival\Desktop\json\ex5.json','w') as out:
    json.dump(ex5_properties,out,indent=4)

