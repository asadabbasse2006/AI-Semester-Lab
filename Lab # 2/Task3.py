myDict = {"Asad Abbas":"30-12-2006","Junaid Ashraf":"19-06-2005","Mannan Khan":"26-08-2004"}
print("Welcome to the birthday dictionary. We know the birthdays of: \nAsad Abbas\nMannan Khan\nJunaid Ashraf")
name = input("Who's birthday do you want to look up?")
if name in myDict:
    print(name, " birthday's is ",myDict[name])
