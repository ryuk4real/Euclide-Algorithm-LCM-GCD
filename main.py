
'''
This program let you calculate:
    - the least common multiple between two numbers
    - the greates common divisor between two numbers
    - the euclidean algorithm between two numbers
    - print the list of the commands
    - exit the program :)
'''




def __main__():
    import eucl
    import lcm
    import gcd

    action = "___"

    #-------------------------------------------
    #MENU STRINGS
    #-------------------------------------------
    menu =  [   "█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█",
                "█ Commands:  lcm: least common multiple between two numbers             █",
                "█            gcd: greatest common divisor between two numbers           █",
                "█            eucl: euclidian algorithm between two numbers              █",
                "█            commands: list of all commands                             █",
                "█            exit: close the program                                    █",
                "▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀"]
    #-------------------------------------------

    #Print the menu
    PrintMenu(menu)

    #Menu loop
    while True:
        
        #request the command from the user
        print(" ")
        action = input("Insert a command:")

        #check commands

        #exit program
        if action == "exit":
            break


        #print commands
        elif action == "commands":
            PrintMenu(menu)


        #Euclidiean algorithm 
        elif action == "eucl":
            eucl.eucl()

        #great common divisor
        elif action == "gcd":
            gcd.gcd()
        
        #least common multiple
        elif action == "lcm":
            lcm.lcm()

        #wrong input
        else:
            print("This command doesn't exist :)")



def PrintMenu(menu):
    x = 0
    for x in range(0, len(menu)):
        print(menu[x])
        x += 1

__main__()