try:
    r = int(input("Enter a number : "))
    print(r)

except ValueError as x :
    print("The exception is " , x )