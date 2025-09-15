sample = {("Sohaib","Ali"):"023456789433", ("Aib","Ali"):"92309238322384"}
firstName = input("Enter First Name: ")
lastName = input("Enter Last Name: ")
searchTuple = (firstName, lastName)
if searchTuple in sample:
    print(sample[searchTuple])
else:
    print("Name not found")