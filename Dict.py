
# Dictionary methods

"""
students = {}

print(type(students))
"""

# students = {"Name" : "Om", "stud_id":121, "city":"pune", "marks":79.20}

#print(students)

# D = students.copy()

"""
# update Name
students["Name"] = "Ram"

print(students)
"""

# update stud_id using update function

"""students.update({"stud_id": 122})
print(students)
"""


"""
# print all kets

A = students.keys()

print(A)

print(type(A))
"""


"""
# items function 
  
    print the key and value seperately.


students = {"Name" : "Om", "stud_id":121, "city":"pune", "marks":79.20}


print(students.items())

"""


"""
# keys() Function

#Returns all keys from the dictionary. 

students = {"Name" : "Om", "stud_id":121, "city":"pune", "marks":79.20}

K = students.keys()

print(K)

"""


"""
# value function()

# Returns all values from the dictionary. 

students = {"Name" : "Om", "stud_id":121, "city":"pune", "marks":79.20}

print(students.values())

"""


"""
# get Function

# Returns the value of a particular key.

students = {"Name" : "Om", "stud_id":121, "city":"pune", "marks":79.20}

print(students.get("Name"))

"""
"""
# pop() function
# Removes a specified key and returns its value.

students = {"Name" : "Om", "stud_id":121, "city":"pune", "marks":79.20}

students.pop("city")

print(students)

"""
"""
# popitem() function

# Removes and returns the last inserted key-value pair.

students = {"Name" : "Om", "stud_id":121, "city":"pune", "marks":79.20}

A = students.popitem()
print(A)

students.popitem()
print(students)
"""


"""
# clear() function

# remove all key value pairs from dictionary and provide empty list.

students = {"Name" : "Om", "stud_id":121, "city":"pune", "marks":79.20}

students.clear()
print(students)

"""



"""
# setdefault() Function
# Returns the value of a key. If the key does not exist, it inserts the key with the given default value.
students = {"Name" : "Om", "stud_id":121, "city":"pune", "marks":79.20}

students.setdefault("age" , 23)
print(students)

"""

"""
# fromkeys() Function
# Creates a new dictionary using given keys and a common default value.

students = ["Name","Age","City"]

D = dict.fromkeys(students,0)

print(D)

"""
