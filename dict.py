# dictionaries in python
my_car = {
    "brand": "ford",
    "model": "mustang",
    "year": 1964,
    "color": "red"
} 
#accessing dictionary
x= dict(name='kofi', age=22)
# print(x)
# print(my_car)

#accessing values
model = my_car.get("model")
print(model)

#calling the key [key]
color =my_car["color"]
print(color)

# using the .key method helps finds all keys in the dictonary
allKeys = my_car.keys()
print(allKeys)

# using the .values method helps finds all values in the dictonary
allValues = my_car.values()
print(allValues)

# using the .items method helps finds all items in the dictonary
allItems = my_car.items()
print(allItems)

# chaging valuesin a dictionary
# use the .update method
my_car.update ({"year": 2020})
print(my_car)
# adding a new key value is also under update
my_car.update({"transmission": "auto"})
print(my_car)

my_car["airbag"]= True
print(my_car)

# deleting a key value pair
my_car.pop("airbag")
print(my_car)

student_directory = {

}

st_1 = {
    "name": "kofi",
    "age": 22,
    "class" : "btech"
}
st_2 = {
    "name": "manye",
    "age": 25,
    "class" : "d.eng"

}
st_3 = {
    "name": "sereoah",
    "age": 22,
    "class" : "d.food"
}
# nested dictioniary
student_directory.update({1:st_1, 2:st_2, 3:st_3})
# print(student_directory)

for students in student_directory.values():
    all_names = students["name"] 
print(all_names)