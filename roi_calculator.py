class ROI_Calculator():

    def income(self):
        print("Let's calculate your monthly income.\n")
        rental = int(input("\nFirst, what is your monthly rental income? \n\n"))
        laundry = int(input("\nSecond, what is your monthly laundry income? \n\n"))
        storage = int(input("\nThird, what is your monthly storage income? \n\n"))
        misc = int(input("\nLast, what is your monthly miscellaneous income? \n\n"))
        monthly_income = rental + laundry + storage + misc
        print(f"\nYour total monthly income is ${monthly_income}.\n")
        return monthly_income

    def expenses(self):
        print("\nLet's calculate your monthly expense.\n")
        tax = int(input("\nWhat is your monthly taxes? \n\n"))
        insurance = int(input("\nWhat is your monthly insurance? \n\n"))
        utilities = int(input("\nWhat is your monthly utilities? \n\n"))
        homeowners = int(input("\nWhat is your monthly homeowners association? \n\n"))
        lawn_snow = int(input("\nWhat is your monthly lawn and snow? \n\n"))
        vacancy = int(input("\nWhat is your monthly vacancy? \n\n"))
        repair = int(input("\nWhat is your monthly repairs? \n\n"))
        capital_exp = int(input("\nWhat is your monthly capital expenditures? \n\n"))
        prop_man = int(input("\nWhat is your monthly property management? \n\n"))
        mortgage = int(input("\nWhat is your monthly mortgage payment? \n\n"))
        monthly_expenses = tax + insurance + utilities + homeowners + lawn_snow + vacancy + repair + capital_exp+ prop_man + mortgage
        print(f"\nYour total monthly expenses are ${monthly_expenses}.\n")
        return monthly_expenses
    
    def cash_flow(self,monthly_income,monthly_expenses):
        self.monthly_income = monthly_income
        self.monthly_expenses = monthly_expenses
        monthly_cashflow = monthly_income - monthly_expenses
        annual_cashflow = monthly_cashflow * 12
        print(f"\nYour monthly cashflow is ${monthly_cashflow},your annual cashflow ${annual_cashflow}.\n")
        return annual_cashflow
    
    
    def calculate_ROI(self, annual_cashflow):
        self.annual_cashflow = annual_cashflow
        print("\nWe will now calculate ROI.\n")
        downpayment = int(input("\nWhat is the downpayment? \n\n"))
        closing_cost = int(input("\nWhat is the closing costs? \n\n"))
        rehab = int(input("\nWhat is the rehab budget? \n\n"))
        investment = downpayment + closing_cost + rehab
        ROI = self.annual_cashflow / investment
        ROI_percentage = ROI * 100
        print(f"\nYour return on investment is {ROI_percentage}%.\n")
        
def run():
    print("\nLet's check the return on investment.")
    roi_calculator = ROI_Calculator()
    monthly_income = roi_calculator.income()
    monthly_expenses = roi_calculator.expenses()
    annual_flow = roi_calculator.cash_flow(monthly_income, monthly_expenses)
    roi_calculator.calculate_ROI(annual_flow)

run()