import json

file_path = r"F:\Mithun-PythonCode\Python\Materials\session0408-filehandeling\Code\files\files\user.json"


def update_user_age(file_path, user_id, new_age):
    # 1. Read and print prior (original) content
    print("Prior file or original content:")
    with open(file_path, 'r') as f:
        users = json.load(f)
        print(json.dumps(users, indent=2))

    # 2. Update the age
    for user in users:
        if user['id'] == user_id:
            user['age'] = new_age
            break

    # 3. Save the updated list back to the file
    with open(file_path, 'w') as f:
        json.dump(users, f, indent=2)

    print(f"\nUpdated user with ID {user_id} to age {new_age}")

    # 4. Read and print updated content to verify
    print("\nUpdated file content:")
    with open(file_path, 'r') as f:
        print(json.dumps(json.load(f), indent=2))


# Call the function from the global scope (unindented)
update_user_age(file_path, 3, 35)
