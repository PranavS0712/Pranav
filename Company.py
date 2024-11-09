from Employee import Employee, SalaryEmployee,HourlyEmployee,CommissionEmployee

class Company :
    def __init__(self):
        self.employees = []
    
    def add_employee(self,new_employee):
        self.employees.append(new_employee)
    
    def display_employees(self):
        print('Current Employees:')
        for i in self.employees:
            print(i.fname,i.lname)
        print('____________')

    def pay_employees(self):
        print('Paying Employees:')
        for i in self.employees:
                    print('Paycheck for :', i.fname,i.lname)
                    print(f'Amount: $ {i.calculate_paycheck():,.2f}')
                    print('------------')

def main():
    my_company = Company()

    employee1 = SalaryEmployee('Pranav', 'S', 90000)
    my_company.add_employee(employee1)
    employee2 = HourlyEmployee('Pratheek', 'MK',25,50)
    my_company.add_employee(employee2)
    employee3 = CommissionEmployee('Sowmya', 'D', 700000 , 5, 30)
    my_company.add_employee(employee3)

    my_company.pay_employees()

main() 

