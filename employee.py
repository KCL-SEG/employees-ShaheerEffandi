"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""
import contracts

class Employee:

    def __init__(self, name, *contracts):
        self.name = name
        self.contracts = []
        for contractType in contracts:
            self.contracts.append(contractType)


    def get_pay(self):
        totalPay = 0
        for contract in self.contracts:
            totalPay += contract.getPay()
        return totalPay

    def __str__(self):
        payString = f"{self.name} works on a "
        for i in range(len(self.contracts)):
            payString += str(self.contracts[i])
            if i < len(self.contracts) - 1:
                payString += " and receives a "


        payString += f".  Their total pay is {self.get_pay()}."
        return payString


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
b_contract = contracts.SalaryContract(4000)
billie = Employee('Billie', b_contract)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
c_contract = contracts.HourlyContract(25, 100)
charlie = Employee('Charlie', c_contract)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
r_contract = contracts.SalaryContract(3000)
r_contract_commission = contracts.CommissionContract(200, 4)
renee = Employee('Renee', r_contract, r_contract_commission)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
j_contract = contracts.HourlyContract(25, 150)
j_contract_commission = contracts.CommissionContract(220, 3)
jan = Employee('Jan', j_contract, j_contract_commission)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
ro_contract = contracts.SalaryContract(2000)
ro_bonus_contract = contracts.BonusContract(1500)
robbie = Employee('Robbie', ro_contract, ro_bonus_contract)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
a_contract = contracts.HourlyContract(30, 120)
a_bonus_contract = contracts.BonusContract(600)
ariel = Employee('Ariel', a_contract, a_bonus_contract)
