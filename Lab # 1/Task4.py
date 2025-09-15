marks = int(input("Enter marks: "))
if 0 <= marks <= 100:
    if 90 <= marks <= 100:
        print("The grade is A")
    elif 80 <= marks <= 90:
        print("The grade is B")
    elif 70 <= marks <= 80:
        print("The grade is C")
    elif 60 <= marks <= 70:
        print("The grade is D")
    elif 50 <= marks <= 60:
        print("The grade is E")
    else:
        print("The grade is F")
else:
    print("Marks can never be greater than 100")