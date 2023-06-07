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

batter = {
        "id": "0004",
		"type": "donut",
		"name": "Old Fashioned",
		"ppu": 0.55,
		"batters":
			{
				"batter":
					[
						{ "id": "1001", "type": "Regular" },
						{ "id": "1002", "type": "Chocolate" }
					]
			},
           "topping":
			[
				{ "id": "5001", "type": "None" },
				{ "id": "5002", "type": "Glazed" },
				{ "id": "5003", "type": "Chocolate" },
				{ "id": "5004", "type": "Maple" }
			],
            "id": "0005",
		"type": "coffee",
		"name": "Old Fashioned",
		"ppu": 0.55,
		"batters":
			{
				"batter":
					[
						{ "id": "1001", "type": "Regular" },
						{ "id": "1002", "type": "Chocolate" }
					]
			},
           "topping":
			[
				{ "id": "5001", "type": "None" },
				{ "id": "5002", "type": "Glazed" },
				{ "id": "5003", "type": "Chocolate" },
				{ "id": "5004", "type": "Maple" }
			]

	}

with open(r'C:\Users\sival\Desktop\json\ex5.json', 'w') as f:

    json.dump(batter, f)


