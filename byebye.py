valid = False
while not valid :
    try :
        x = int(input("Enter a number : "))
        while x % 2 == 0 :
             print("bye")
             break
             valid = True
    except ValueError :
        print("Invalid")
        