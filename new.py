import json
with open("hello.json", mode="r", encoding="utf-8") as input_file:
     original_json = input_file.read()


json_data = json.loads(original_json)
mini_json = json.dumps(json_data, indent=6, separators=(",", ":"))
with open("new.json", mode="w", encoding="utf-8") as output_file:
     output_file.write(mini_json)
