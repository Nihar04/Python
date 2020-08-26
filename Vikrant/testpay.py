import hr, employees, productivity, contacts

manager = employees.Manager(1, 'john smith', 1500)
manager.address = contacts.Address(
    '121 Admin Road',
    'Concord',
    'NH',
    '03301'
)

secretary = employees.Secretary(2, 'Jane Doe', 1200)
secretary.address = contacts.Address(
    '67 Paperwork Ave',
    'Manchester',
    'NH',
    '03301'
)

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

# Composition and Inheritance
