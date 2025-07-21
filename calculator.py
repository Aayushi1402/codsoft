def addition(x,y):
    return x+y
def substraction(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    return x/y
print("SELECT OPERATION:")
print("1.ADDITION")
print("2.SUBSTRACTION")
print("3.MULTIPLICATION")
print("4.DIVISION")

option=int(input("SELECT OPERATION(1-4):"))
           
x=int(input("Enter first number:"))
y=int(input("Enter second number:"))

if option==1:
    print(x,'+',y,'=',addition(x,y))
elif option==2:
    print(x,'-',y,'=',substraction(x,y))
elif option==3:
    print(x,'*',y,'=',multiplication(x,y))
elif option==4:
    print(x,'/',y,'=',division(x,y))
