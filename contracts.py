#Essentially an abstract class
class Contract:
    def getPay(self):
        pass

class SalaryContract(Contract):
    def __init__ (self, monthlySal):
        self.monthlySal = monthlySal

    def __str__ (self):
        return f"monthly salary of {self.getPay()}"

    def getPay(self):
        return self.monthlySal


class HourlyContract(Contract):
    def __init__ (self, hourlyPay, hoursPerMonth):
        self.hourlyPay = hourlyPay
        self.hoursPerMonth = hoursPerMonth

    def __str__ (self):
        return f"contract of {self.hoursPerMonth} hours at {self.hourlyPay}/hour"

    def getPay(self):
        return self.hourlyPay * self.hoursPerMonth

#Both hourly and Commision are the same code-wise
#But since they are both for different scenarioes we should separate them
class CommissionContract(Contract):
    def __init__ (self, commisionRate, numberOfCommissions):
        self.commisionRate = commisionRate
        self.numberOfCommissions = numberOfCommissions

    def __str__ (self):
        return f"commission for {self.numberOfCommissions} at {self.commisionRate}/contract"

    def getPay(self):
        return self.commisionRate * self.numberOfCommissions

class BonusContract(Contract):
    def __init__ (self, bonus):
        self.bonus = bonus

    def __str__ (self):
        return f"bonus commision of {self.bonus}"

    def getPay(self):
        return self.bonus
