import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
yumMachine = SandwichMaker(data.resources)
choice = ''
myCashier = Cashier()




def main():
    closed = True
    closedO = True
    loop = True
    while loop:
        while closedO:
            closed = True
            while closed:
                menuChoice = input("What would you like? (small/medium/large/off/report):")
                if menuChoice == "small":
                    choice = data.recipes["small"]
                    closed = False
                elif menuChoice == "medium":
                    choice = data.recipes["medium"]
                    closed = False
                elif menuChoice == "large":
                    choice = data.recipes["large"]
                    closed = False
                elif menuChoice == "report":
                    print(data.resources)
                    closed = True
                elif menuChoice == "off":
                    exit()
                else:
                    print('Please, choose from one of the options')

            if (menuChoice == "small" or menuChoice == "medium" or menuChoice == "large"):
                coins = myCashier.process_coins(choice)
                tranApproved = myCashier.transaction_result(coins, choice["cost"])
                if tranApproved:
                    closedO = False
                else:
                    closed0 = True

        data.resources = yumMachine.make_sandwich(choice["ingredients"], resources,data.resources)
        closedO = True

if __name__=="__main__":
    main()