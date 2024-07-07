import json

data = {
    "user":{
        "name": "Will Byers",
        "age": 34
    }
    
}

store = {
    "cutomers": {

        "player" : "swati",
        "group": 50


    }
}

with open("data_file.json" , "w") as write_file:
    json.dump(data, write_file, indent=4)
    json.dump(store, write_file, indent=4)

json_str = json.dumps(data, indent = 4)

json_str = json.dumps(store, indent = 4)
print(json_str)