import json
from pathlib import Path

# Resolve path relative to this script's directory
json_path = Path(__file__).parent / "student_backup.json"

with open(json_path, "r") as file:
    data = json.load(file)
    # print(data)
    for i in data:
        print(f"Name: {i['name']}", f"Marks: {i['marks']}", f"City: {i['city']}", sep="|")
