groceryList = ["eggs", "bananas", "peas", "milk"]
print("Please grab some " + groceryList[3] + " from the store, Thanks!")
#lists with brackets  #tuples cant be changed and uses {} instead of [] and are in order
customers = [
    "Jack Smith",
    "John Smith",
    "Jane Smith",
    "Jim Smith",
    "Jess Smith",
    "Jet Smith",
    "Jason Smith",
    "Johnny Smith",
    "Jerry Smith"
]
print(customers)

#Multidimensional Lists

#Daily high and low temps
temps = [
     [99, 65],
     [104, 88],
    [107, 91]
]
print(temps[2])

#Dictionaries are indexed list of values like sets surround with {} and doesnt allow duplicates
customer1 = {
    "name:Jim Smith",
    "age: 44",
    "height: 65 inches",
    "sex: male"
}
customer2 = {
    "name:Jane Smith",
    "age: 64",
    "height: 69 inches",
    "sex: female"
}
allcustomers = customer1 , customer2
print(allcustomers)