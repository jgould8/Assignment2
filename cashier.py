class Cashier:
    def __init__(self):
        """Receives resources as input.
           Hint: bind input variable to self variable"""


    def process_coins(self,choice):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        cost = choice["cost"]
        self.numDollars = float(input("How many dollars do you have?: "))
        self.numHalfDollars = float(input("How many half dollars?: "))
        self.numQuarters = float(input("how many quarters?: "))
        self.numNickels = float(input("how many nickels?: "))
        self.payment = (1.00 * self.numDollars)+ (0.50 * self.numHalfDollars) + (0.25 * self.numQuarters) + (0.00 * self.numNickels)
        return self.payment

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""

        self.result = coins - cost
        if self.result > 0:
            print("Your change is: ", self.result)
            return True
        if self.result < 0:
            print("not enough money.")
            return False
        else:
            print("exact change.")
            return True