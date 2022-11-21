# %%
rentalprice = int(input("What is the price of your rental property?").replace(',',""))
class Rental_ROI(): 
    def __init__(self, rentalprice):
        self.total_monthly_income = 0
        self.total_monthly_expenses = 0
        self.total_monthly_cash_flow = 0
        self.total_annual_cash_flow = 0
        self.total_investment = 0
        self.return_on_investment = 0
    

    def income(self):
        self.rental_income = int(input('What is your monthly rental income?'))
        if self.rental_income >= 0:
            print(f"Monthly rental income is ${self.rental_income}")
        else:
            print("That is not a valid amount. Please try again.")
        
        self.laundry = int(input('What is your laundry income?'))
        if self.laundry >= 0:
            print(f"Monthly laundry income is ${self.laundry}")
        else:
            print("That is not a valid amount. Please try again.")

        self.storage = int(input('What is your storage income?'))
        if self.storage >= 0:
            print(f"Monthly storage income is ${self.storage}")
        else:
            print("That is not a valid amount. Please try again.")

        self.misc = int(input('What is your misc income?'))
        if self.misc >= 0:
            print(f"Monthly storage income is ${self.misc}")
        else:
            print("That is not a valid amount. Please try again.")

        self.total_monthly_income = self.rental_income + self.laundry + self.storage + self.misc
        print(f"The total monthly income is ${self.total_monthly_income}")


    def expenses(self):
        self.taxes = int(input('How much are your taxes?'))
        if self.taxes >= 0:
            print(f"Monthly taxes are ${self.taxes}")
        else:
            print("That is not a valid amount. Please try again.")

        self.insurance = int(input('How much is your insurance?'))
        if self.insurance >= 0:
            print(f"Monthly insurance is ${self.insurance}")
        else:
            print("That is not a valid amount. Please try again.")
        
        self.utilites = int(input('How much are your utilities?'))
        if self.utilites >= 0:
            print(f"Monthly utilities are ${self.utilites}")
        else:
            print("That is not a valid amount. Please try again.")

        self.HOAfees = int(input('How much are your HOA fees?'))
        if self.HOAfees >= 0:
            print(f"Monthly HOA fees are ${self.HOAfees}")
        else:
            print("That is not a valid amount. Please try again.")

        self.lawnsnow = int(input('How much is your lawncare and/or snow removal?'))
        if self.lawnsnow >= 0:
            print(f"Monthly lawn and/or snow cost is ${self.lawnsnow}")
        else:
            print("That is not a valid amount. Please try again.")

        self.vacancy = int(input('How much is your vacancy?'))
        if self.vacancy >= 0:
            print(f"Monthly vacancy is ${self.vacancy}")
        else:
            print("That is not a valid amount. Please try again.")

        self.repairs = int(input('How much are your repairs?'))
        if self.repairs >= 0:
            print(f"Monthly repair is ${self.repairs}")
        else:
            print("That is not a valid amount. Please try again.")

        self.capital_exp = int(input('How much is your capital expenditure?'))
        if self.capital_exp >= 0:
            print(f"Monthly capital expenditure is ${self.capital_exp}")
        else:
            print("That is not a valid amount. Please try again.")

        self.property_management = int(input('How much is your property management?'))
        if self.property_management >= 0:
            print(f"Monthly property management fee is ${self.property_management}")
        else:
            print("That is not a valid amount. Please try again.")

        self.mortgage = int(input('How much is your mortgage?'))
        if self.mortgage >= 0:
            print(f"Monthly mortgage is ${self.mortgage}")
        else:
            print("That is not a valid amount. Please try again.")
        

        self.total_monthly_expenses = self.taxes + self.insurance + self.utilites + self.HOAfees + self.lawnsnow + self.vacancy + self.repairs + self.capital_exp + self.property_management + self.mortgage
        print(f"The total monthly expense is ${self.total_monthly_expenses}")
    
   
    def cashflow(self):
        self.total_monthly_cash_flow = self.total_monthly_income - self.total_monthly_expenses
        print(f"The total monthly cash flow is ${self.total_monthly_cash_flow}")

        
    def cashreturn(self):
        self.down_payment = int(input('How much is your down payment?').replace(',',""))
        if self.down_payment >= 0:  
             print(f"The down payment is ${self.down_payment}")
        else:
            print("That is not a valid amount. Please try again.")

        self.closing_cost = int(input('How much is your closing costs?').replace(',',""))
        if self.closing_cost >= 0:
            print(f"The closing cost is ${self.closing_cost}")
        else:
            print("That is not a valid amount. Please try again.")

        self.rehab_budget = int(input('How much is your rehab budget?').replace(',',""))
        if self.rehab_budget >= 0:
            print(f"The rehab budget is ${self.rehab_budget}")
        else:
            print("That is not a valid amount. Please try again.")


        self.misc_other = int(input('How much are your misc costs?'))  
        if self.misc_other >= 0:
            print(f"The misc other is ${self.misc_other}")
        else:
            print("That is not a valid amount. Please try again.")
        
        self.total_investment = self.down_payment + self.closing_cost + self.rehab_budget + self.misc_other
        print(f"The total investment is ${self.total_investment}")

        self.total_annual_cash_flow = self.total_monthly_cash_flow * 12
        print(f"The total annual cash flow is ${self.total_annual_cash_flow}")

        self.return_on_investment = (self.total_annual_cash_flow / self.total_investment) * 100
        print(f"The cash on cash ROI is {self.return_on_investment} %")
    

    def runner(self):
        while True:
            response = (input("Would you like to calculate the ROI of your Rental Property? Please enter yes or no to continue")).lower()
            if response == "yes":
                self.income()
                self.expenses()
                self.cashflow()
                self.cashreturn()
                break
            elif response == "no":
                print("Thanks! Have a nice day.")
                break
            else:
                print("Input not valid. Try again.")


person1 = Rental_ROI(" ")
person1.runner()



# %%
