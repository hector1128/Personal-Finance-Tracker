db = open("test.txt", "r")
lines = db.readlines()
db.close()

info = {}  # Main dictionary to store user information

# For each line in the file
for line in lines:
    line = line.strip()
    entries = line.split(", ")  # Split each line by comma-space for key-value pairs
    print(entries)
    user_info = {}  # Temporary dictionary for each user's info
    
    for item in entries:
        key, value = item.split(": ")  # Separate key and value by ": "
        user_info[key.strip()] = value.strip()  # Add to the user's dictionary
    
    # Assuming the 'username' is the unique identifier for each user:
    username = user_info.get("username", None)
    if username:
        info[username] = user_info  # Store user's info dictionary with their username as the key

# Example: print the dictionary to verify
print(info)

    








        

    

