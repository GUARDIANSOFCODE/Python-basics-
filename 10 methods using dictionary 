my_dict = {"name": "Alice", "age": 30, "city": "New York"}

# 1. keys() - Returns a view of all keys in the dictionary
print("Keys:", my_dict.keys())

# 2. values() - Returns a view of all values in the dictionary
print("Values:", my_dict.values())

# 3. items() - Returns a view of all key-value pairs as tuples
print("Items:", my_dict.items())

# 4. get(key, default=None) - Returns the value for the given key, or default if not found
print("Value for 'age':", my_dict.get("age"))
print("Value for 'job' (not found):", my_dict.get("job", "Not Found"))

# 5. pop(key, default=None) - Removes the item with the given key and returns its value
#    (optional default value if not found)
value = my_dict.pop("city")
print("Removed 'city':", value)
# print(my_dict.pop("city"))  # This will raise KeyError

# 6. popitem() - Removes and returns an arbitrary key-value pair
key, value = my_dict.popitem()
print("Removed arbitrary item:", key, value)

# 7. update(other_dict) - Updates the dictionary with key-value pairs from another dictionary
other_dict = {"job": "Software Engineer"}
my_dict.update(other_dict)
print("Updated dictionary:", my_dict)

# 8. clear() - Removes all items from the dictionary
my_dict.clear()
print("Dictionary after clear():", my_dict)

# 9. copy() - Returns a shallow copy of the dictionary
new_dict = my_dict.copy()  # Since my_dict is now empty, this will also be empty
print("Shallow copy:", new_dict)

# 10. fromkeys(seq, value=None) - Creates a new dictionary with keys from seq and values set to value
seq = ("x", "y", "z")
new_dict = dict.fromkeys(seq, 0)
print("Dictionary from keys:", new_dict)
