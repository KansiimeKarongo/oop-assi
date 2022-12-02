 
name=str(input("Enter your name"))
 
if name=="Jack" and name=="Jackie":
    print(f"Hello {name},GoodMorning")
    print("Goodbye!!")
else:
    print("Hello friend")
    age=int(input("Enter your age: "))
    
    if age < 18:
        print("Below age of working")
    elif age > 18 and age < 25:
        print("Look for a Job")

    elif age >=25 and age < 30:
        print("You should be having a job already")

    elif age > 30 and age < 60:
        print("You should think of having a family")
    elif age < 90 and age >=60:
        print("You should retire!")

    else: 
        print(f"Goodbye , your name is {name} and your {age} years old")