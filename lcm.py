def lcm():
    #calculate the least common multiple

    #take two numbers from input
    num1 = int(input("Insert the first integer: "))
    num2 = int(input("Insert the second integer: "))

    #save these numbers for later
    n1 = num1
    n2 = num2

    #set the reminder different from 0 :)
    reminder = -9999999999999

    #find greater num from num1 and num2
    if num1-num2 < 0:
        greater = num2
        num2 = num1
        num1 = greater
    #-----------------------------------

    #loop that calculate the quotient, the divisor and the reminder
    while reminder != 0:
        mid_result = num1 // num2
        reminder = num1 % num2

        if reminder != 0:
            num1 = num2
            num2 = reminder
    
    #easy way to calculate the least common multiple by dividing the
    # absolute value of the product of the two numbers by the greatest
    #common divisor

    lcm = abs(n1*n2)//num2

    #print the result between two new lines, and we're done :)
    print(" ")
    print(">>>","LCM(", n1, ",", n2, ") =" , lcm)
    print(" ")
    return 0
