# A dictionary is a data type yhat stores data in terms  of key-value
#It is introduced by the use of carlybraces
# The values stored inside a dictionary
#To acces the values of a dictionary we use the keys

phonebook = {
    "Makiso" : "25437777826",
    "Quinn" :"254367898",
    "Alvin" : " 25438736"
}

#showing the whole dictionary
print(phonebook)
print(type(phonebook))

#print out makiso's number
print(phonebook["Makiso"])

print('=============')

player = {
    "Name" : "Messi",
    "Age" : "30",
    "Teams" : ["PSG", "Barselona" , "Argentina"],
    "more" : {
        "children" : 3,
        "residence": "US",
        "phone" : (25467383, 25476895, 254766975)

    }
}

#print barselona a team he played for 
print(player)
print(type(player))
print(player["Teams"][1])

print("Messi's second number:",player["more"] ["phone"][1])