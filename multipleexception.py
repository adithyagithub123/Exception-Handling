try :
    x = int(input("Enter first number : "))
    y = int(input("Enter second number : "))

    result = x/y
    print(result)
    print(result1)

except ZeroDivisionError as t :
    print("Division by 0 is not allowed " , t)

except ValueError as r :
    print("Please enter an integer number ", r)

except NameError as e :
    print("Invalid variable " , e)

finally :
    print("I will execute no matter what")