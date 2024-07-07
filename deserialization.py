import json

# JSON string
json_string = '{"name": "John", "age": 30, "city": "New York"}'

# Parse JSON string into a Python dictionary
data = json.loads(json_string)

# Print the dictionary
print(data)
print(data['name'])  # Accessing a value
