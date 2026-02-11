#Python list
#A lit is acollection of items that are colleceted in a sertain way
#A list is introduced by the use of the square brackets {}
#The iems of a list are stored ininbexes. Note: In programming we strart from index zero , bmw, benz, audi
#A list is mutable i.e the contents of a list can be changed

cars = ("BMW", "Benz", "Audi", "Prado", "Ford", "Rollroys", "Mc Laren",)
print(cars)
print(type(cars))

#Accessing items off a list
print(cars[2])
print("The cars on index four is ", cars[4])

#List Slicing
#This is creating a list from an even bigger list
print(cars[4:])

#Printing from index 0 to 3 
print(cars[:4])

#printing from benz to mc laren
print(cars[1:5])

#List mutability
#we use the function uphend to add an item at the end of a list
cars.append("Mercedes")
print(cars)
cars.append("Subaru")
print(cars)

# we use pop to remove items at the ne of a list
cars.pop()

#we can use an inex to add items to a list
cars[5] = "Pajero"
print(cars)

# we use sort to arrange animals in alphabetical order
cars.sort()
print(cars)