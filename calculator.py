#Taking the input from user 

first = input ("enter 1st number: ")
operator = input( "enter operator (+, -,*,/,%)")
second= input("enter 2nd number: ")

#Converting srting into numbers 

first= int(first)
second=int(second)

#Using  IF statement
if operator == "+":
    print(first + second)

#Using elif statement (the next condition will run only of the above condition is false )
    
elif operator == "-":
    print(first - second)
elif operator== "*":
    print(first * second)
elif operator=="/":
    print(first / second)
elif operator== "%":
    print(first % second)
else: print("invalid operations")