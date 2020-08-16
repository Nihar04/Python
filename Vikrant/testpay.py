import hr, employees, productivity

manager = employees.Manager(1, 'john smith', 1500)
secretary = employees.Secretary(2, 'Jane Doe', 1200)
sales_guy = employees.SalesPerson(3, 'kevin bacon', 1500, 250)
factory_worker = employees.FactoryWorker(4, 'Pete', 40, 15)

employees = [

        manager,
        secretary,
        sales_guy,
        factory_worker
]

productivity_system = productivity.ProductivitySystem()
productivity_system.track(employees, 40)


payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll(employees)

# Multiple Inheritance
