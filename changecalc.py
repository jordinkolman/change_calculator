'''
Created on Wednesday Jul 07 11:06 2022

@author: Jordin Kolman
'''
'''
def changeCalc():
    choice = 'y'
    
    # display a welcome message
    print("Change Calculator")
    print()

    while choice.lower() == 'y':
        # get input from user
        cents = int(input('Enter number of cents (0-99): '))
        # calculate the number of quarters
        quarters = cents // 25
        cents = cents % 25 # assign the remainder to the cents variable
        # caclulate the number of dimes
        dimes = cents // 10
        cents = cents % 10 # assign the remainder to the cents variable
        # calculate the number of nickels and pennies
        nickels = cents // 5
        pennies = cents % 5 # assign the remainder to pennies as thats the only denomination left

        # display coins
        print("Quarters: "  + str(quarters))
        print("Dimes: "  + str(dimes))
        print("Nickels: "  + str(nickels))
        print("Pennies: "  + str(pennies))
        print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print('Bye!')
'''

def changeCalcv2():
    choice = 'y'

    # display a welcome message
    print("Change Calculator")
    print()

    while choice.lower() == 'y': # .lower method converts input to lowercase to avoid syntax issues
        # get input from user
        total = float(input('Please enter the total cost (up to 100): '))
        if total > 100:
            print("Error: total is too high. ")
            break
        payment = float(input('Please enter the total given by customer (up to 100): '))
        if payment > 100:
            print("Error: Payment is too high. ")
            break
        # calculate the change owed to customer
        change = round((payment - total), 2)
        print("Your change is: " + str(change))
        # calculate the denominations
        twenties = int(change // 20)
        change = change % 20

        tens = int(change // 10)
        change = change % 10

        fives = int(change // 5)
        change = change % 5

        ones = int(change // 1)
        change = change % 1

        coins = change * 100

        quarters = int(coins // 25)
        coins = coins % 25

        dimes = int(coins // 10)
        coins = coins % 10

        nickels = int(coins // 5)
        pennies = int(coins % 5)

        #display change
        print ("Denominations: ")
        print("20s: " + str(twenties))
        print("10s: " + str(tens))
        print("5s: " + str(fives))
        print("1s: " + str(ones))
        print("Quarters: " + str(quarters))
        print("Dimes: " + str(dimes))
        print("Nickels: " + str(nickels))
        print("Pennies: " + str(pennies))
        print()

        #see if user wants to continue
        choice = input("Continue? (y/n): ")
        print()
    
    print("Bye!")

changeCalcv2()