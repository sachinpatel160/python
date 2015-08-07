def print_name(a):
    print("Hello",a)

a=input("Enter your name: ")
#called function
print_name(a)
def cost(h,d,m):
    c_rs=h*d*m*2
    return c_rs
h=24
d=12
m=60
print('''Shutup!
Total time of mine is wasted is: ''',cost(h,d,m))
