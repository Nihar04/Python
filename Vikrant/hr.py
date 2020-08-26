from abc import ABC, abstractmethod

class PayrollSystem:
    def calculate_payroll(self,employees):
        print('Calculating Payroll')
        print('===================')
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- Check Amount:$ {employee.calculate_payroll()}')
            if employee.address:
                print(employee.address)
            print('')


class SalaryPolicy:
    def __init__(self, weekly_salary):
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary

class HourlyPolicy:
    def __init__(self, hours_worked, hours_rate):
        self.hours_worked = hours_worked
        self.hours_rate = hours_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hours_rate

class CommissionPolicy:
    def __init__(self, weekly_salary, commission):
        self.hours_worked = hours_worked
        self.hours_rate = hours_rate

    def calculate_payroll(self):
        return self.weekly_salary + self.commission
