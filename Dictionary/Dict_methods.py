# marks = {
#     "khalid": 100,     #keys:values
#     "Halid ":200,
#     "Rohan":300,
#     0:"Hasan",
#     "lis" :[1,2,3,4,5],
# }
# # print(marks.items())
# # print(marks.keys())
# # print(marks.values())
# # marks.update({"Halid":300})
# # print(marks)
# print(marks.get("Halid"))  #none return
# print(marks["Halid "])   #value of Halid if not exits return erorr
# Creating a sample dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# 1. clear()
# Removes all items from the dictionary
d1 = person.copy()
d1.clear()
print("1. clear():", d1)

# 2. copy()
# Returns a shallow copy of the dictionary
d2 = person.copy()
print("2. copy():", d2)

# 3. fromkeys()
# Creates a new dictionary from given sequence of keys with a specified value
keys = ["a", "b", "c"]
d3 = dict.fromkeys(keys, 0)
print("3. fromkeys():", d3)

# 4. get()
# Returns the value for the specified key
print("4. get('name'):", person.get("name"))
print("4. get('salary', 'Not Found'):", person.get("salary", "Not Found"))

# 5. items()
# Returns a view object of key-value pairs
print("5. items():", list(person.items()))

# 6. keys()
# Returns a view object of keys
print("6. keys():", list(person.keys()))

# 7. pop()
# Removes and returns the value for the specified key
d4 = person.copy()
removed = d4.pop("age")
print("7. pop('age'):", removed)
print("   After pop:", d4)

# 8. popitem()
# Removes and returns the last inserted key-value pair
d5 = person.copy()
last_item = d5.popitem()
print("8. popitem():", last_item)
print("   After popitem:", d5)

# 9. setdefault()
# Returns the value of a key if it exists; if not, inserts the key with a default value
d6 = person.copy()
val = d6.setdefault("gender", "female")
print("9. setdefault('gender', 'female'):", val)
print("   After setdefault:", d6)

# 10. update()
# Updates the dictionary with key-value pairs from another dictionary or iterable
d7 = person.copy()
d7.update({"age": 30, "country": "USA"})
print("10. update():", d7)

# 11. values()
# Returns a view object of values
print("11. values():", list(person.values()))

