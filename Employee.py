class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

class SalaryEmployee(Employee):
    def __init__(self,fname,lname,salary):
        super().__init__(fname,lname)
        self.salary = salary
    
    def calculate_paycheck(self):
        return self.salary/52
    
class HourlyEmployee(Employee):
    def __init__(self,fname,lname,weeklyhours,hourlyrate):
        super().__init__(fname,lname)
        self.weeklyhours = weeklyhours
        self.hourlyrate = hourlyrate

    def calculate_paycheck(self):
        return self.weeklyhours*self.hourlyrate
    
class CommissionEmployee(SalaryEmployee):
    def __init__(self, fname, lname, salary,salesnum,comrate):
        super().__init__(fname, lname, salary)
        self.salesnum = salesnum
        self.comrate = comrate
    
    def calculate_paycheck(self):
        regular_salary = super().calculate_paycheck()
        total_comission = self.salesnum*self.comrate
        return regular_salary + total_comission
