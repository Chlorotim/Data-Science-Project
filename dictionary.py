my_attributes = {"name": "joy", "complexion": "dark", "height": "4.3", "ismarried": False, "name": "uka"}

print(my_attributes.keys())
print(my_attributes.values())
print(my_attributes["complexion"])
print(my_attributes["height"])
print(my_attributes["ismarried"])
print(my_attributes["name"])

# using get to access
print(my_attributes.get("name"))

# change values
my_attributes["complexion"]= "white"
print(my_attributes.get("complexion"))

my_attributes.update({"ismarried": True})
print(my_attributes)

my_attributes.pop("height")
print(my_attributes)

for x in my_attributes:
    print(x) #for the keys
for x in my_attributes:
    print(my_attributes[x]) #for the values

for x in my_attributes.keys():
    print(x)
for x in my_attributes.values():
    print(x)

for x,y in my_attributes.items():
    print(x,y)


# copy dictionaries
vince_attributes = my_attributes.copy()
print(vince_attributes)

# nested dictionaries
vince_family = {
    
    "baby mame": {
        
        "name": "joy", 
        
         "met": 2017
         
         },


    "child1": {
        "name": "kamara", 
        "dob": 2019
        }
               
    }
print(vince_family)

print(vince_family["child1"]["name"])

for x, y in vince_family.items():
    print(x, y)
    