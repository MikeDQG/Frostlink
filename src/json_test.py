import json

input("press any key to start")

# Open the JSON file
with open('../../src/payloads/pasice.json', 'r') as file:
    # Load JSON data from file
    data = json.load(file)

print(data)
print(data[input()])

input("press any key to end")