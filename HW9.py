#Name: Owyn Jones
#Class: 6th Hour
#Assignment: HW9

#1. Print Hello World!
print("Hello World")

#2. Create a dictionary with 3 keys and a value for each key. One of the keys must have a value with a list containing
#three numbers inside.
dictionary = {
    "val1" : 37,
    "val2": "John",
    "val3": [6, 7, 404]
}

#3. Print the keys of the dictionary from #2.
print(dictionary.keys())

#4. Print the values of the dictionary from #2
print(dictionary.values())

#5. Print one of the three numbers from the list by itself
print(dictionary["val3"][1])

#6. Using the update function, add a fourth key to the dictionary and give it a value.
dictionary.update({"val4" : True})

#7. Print the entire dictionary from #2 with the updated key and value.
print(dictionary)

#8. Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information
#within each entry.
nestedDictionary = {
    "person1" : {
        "name" : "Nate",
        "age" : 14,
        "shirt color" : "dark blue",
    },
    "person2" : {
        "name" : "Raphael",
        "age" : 17, #I have no idea how old he actually is, I'm just guessing
        "shirt color" : "red",
    },
    "person3" : {
        "name" : "Owen",
        "age" : 18,
        "shirt color" : "light blue"
    }
}

#9. Print the names of all three classmates on the same line.
print(nestedDictionary["person1"]["name"], nestedDictionary["person2"]["name"], nestedDictionary["person3"]["name"])

#10. Use the pop function to remove one of the nested dictionaries inside and print the full dictionary from #8.
removedPerson = nestedDictionary.pop("person2")
print(nestedDictionary)