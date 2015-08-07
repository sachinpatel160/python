t=eval(input("Enter temperature: "))
while True:
    if t>=31 and t<35:
        print("Sunny day")
        break
    elif t>=35 and t<40:
        print("Warm Day")
        break
    elif t>=40 and t<50:
        print("High Temperature")
        break
    else:
        print("Invalid")
        break
