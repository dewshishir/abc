# Step 1: Creating a dictionary
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print("Created Dictionary:", my_dict)

# Step 2: Printing the dictionary
print("Dictionary:", my_dict)

# Step 3: Accessing dictionary values
name = my_dict["name"]
print("Name:", name)
age = my_dict.get("age")
print("Age:", age)

# Step 4: Finding the length of the dictionary
length = len(my_dict)
print("Length of Dictionary:", length)

# Step 5: Changing a value in the dictionary
my_dict["age"] = 30
print("Updated Dictionary:", my_dict)
