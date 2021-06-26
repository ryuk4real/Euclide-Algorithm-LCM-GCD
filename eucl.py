
def eucl():

    #take two numbers from input
    num1 = int(input("Insert the first integer: "))
    num2 = int(input("Insert the second integer: "))

    #set the reminder different from 0 :)
    reminder = -9999999999999

    print(" ")

    #find greater num from num1 and num2
    if num1-num2 < 0:
        greater = num2
        num2 = num1
        num1 = greater
    #--------------------------------------

    #loop that calculate the quotient, the divisor and the reminder
    while reminder != 0:
        mid_result = num1 // num2
        reminder = num1 % num2

        #print each line
        print('{:<10}{:>12}{:>12}{:>12}{:>12}{:>12}{:>12}'.format(num1," = ",num2," × ",mid_result," + ",reminder))

        #jump when the loop is terminating
        if reminder != 0:
            num1 = num2
            num2 = reminder
    
    #print a new line and we're done
    print(" ")
    return 0