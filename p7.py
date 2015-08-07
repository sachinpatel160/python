#aama for loop ni jaroor nathi pan while condition vaaprie to useful thaay.
t=eval(input("Enter temperature: "))
for t in range(0,50):
    if(t>32 and t<35):
        print("Sunny Day")
        break
    elif(t>35 and t<40):
        print("Warm Day")
        break
    elif(t>40 and t<50):
        print("High Temperature")
        break
    else:
        print("Invalid")
        break
       
