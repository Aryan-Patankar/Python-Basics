print("which action do you what to perfrom?")
a = int(input("1.Addition \n2.Subtraction \n3.Multiplication \n4.Division \n5.Exponent \n6.Floor division \n7.Modulo"))

if a == 1:
    print("Enter 2 integers")
    x = int(input())
    y = int(input())
    print (x + y)
elif a == 2:
    print("Enter 2 integers")
    x = int(input())
    y = int(input())
    print (x - y)
elif a == 3:
    print("Enter 2 integers")
    x = int(input())
    y = int(input())
    print (x * y)
elif a == 4:
    print("Enter 2 integers")
    x = int(input())
    y = int(input())
    print (x / y)
elif a == 5:
    print("Enter 2 integers")
    x = int(input())
    y = int(input())
    print (x ** y)
elif a == 6:
    print("Enter 2 integers")
    x = int(input())
    y = int(input())
    print (x // y)
elif a == 7:
    print("Enter 2 integers")
    x = int(input())
    y = int(input())
    print (x % y)
else:
    print("Enter an interger(s)")