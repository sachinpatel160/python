def name():
    x =input("Enter your name: ")
    print("Hello ",x)
    a=eval(input("Enter value of feedback: "))
    value(a)
def value(a):
    if a==1:
      print("Poor")
    elif a==2:
      print("It's ok!")
    elif a==3:
      print("Good")
    elif a==4:
      print("Very Good")
    elif a==5:
      print("Exellent")
    else:
      print("Please enter a value between 1 to 5")
name()
