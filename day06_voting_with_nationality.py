age = int(input("Enter your age: "))
nationality = input("Enter your nationality: ")

if age >= 18:
    if nationality.lower() == "indian":
        print("You are eligible for voting")
    else:
        print("You are not eligible for voting")
else:
    print("You are not eligible for voting")
