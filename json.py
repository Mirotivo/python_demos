# %% Parsing JSON Data:
import json

json_data = '{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(json_data)

print(data['name'])

# %% Creating JSON Data:
import json

data = {"name": "Alice", "age": 25, "city": "Los Angeles"}
json_data = json.dumps(data)

print(json_data)

# %% Modifying JSON Data:
import json

json_data = '{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(json_data)

data['age'] = 31
updated_json_data = json.dumps(data)

print(updated_json_data)

# %% Adding Data to JSON:
import json

json_data = '{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(json_data)

data['country'] = 'USA'
updated_json_data = json.dumps(data)

print(updated_json_data)

# %% Iterating Over JSON Data:
import json

json_data = '{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(json_data)

for key, value in data.items():
    print(f"{key}: {value}")

# %% Handling Nested JSON:
import json

json_data = '{"person": {"name": "John", "age": 30, "city": "New York"}}'
data = json.loads(json_data)

name = data['person']['name']
print(name)
