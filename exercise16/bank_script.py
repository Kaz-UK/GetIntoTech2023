from users.employee import Employee
from users.customer import Customer
from accounts.current import Current
from accounts.savings import Savings

# Create employee using the Person class, and specific parameters required by employee class
employee1 = Employee("Smith", "Kelly", "32 Cardiff Street, York", "26/01/1982", "ZZ5498H72", 1,
                     "Branch Manager", 52000)
employee2 = Employee("Clarke", "Peter", "59 London Road, York", "13/05/1993", "ZZ96S4752", 2, "Assistant", 32000)
# Set an employee password using setter method
employee1.set_employee_password()
# Pulls information from the employee class (getter method)
employee1.get_employee_name()
# Change employee1 job title
employee1.set_title("Regional Manager")
employee1.get_employee_name()
# Give employee2 a pay rise
employee2.set_salary_increase(5000)
# Employee1 gets married, using Person class to change their name
employee1.set_name("Martin", "Kelly")
# Check employee1 name change
employee1.get_employee_name()
# Find out how many employees work at the bank
print(Employee.number_of_employees)
# Create customer1 using Person class and parameters required by customer class
customer1 = Customer("Fletcher", "Daisy", "67 Bristol Street, York", "02/02/1975", "ZH98S8752", 3, False)
customer2 = Customer("Robinson", "Mark", "85 Glasgow Road, York", "06/01/1985", "ZH99D8974", 4, False)
# See users current credit check status
customer1.get_credit_check()
# Set a credit check for customer1
customer1.set_credit_check()
customer1.get_credit_check()
# Set up a bank account (using existing customer name)
account1 = Current(12548465, "Current", 1000, -500, cust_obj=customer1)
account2 = Current(12548745, "Current", 1500, -1000, cust_obj=customer2)
account3 = Savings(12487454, "Savings", 10000, 4.2, cust_obj=customer1)
account1.get_overview()
account2.get_overview()
# Change name of customer1 to confirm customer data is linked to accounts
customer1.set_name("Thompson", "Daisy")
account1.get_overview()
account3.get_overview()
# Add funds to customer1 current account
account1.set_add_funds()
# Withdraw funds from customer1 current account
account1.set_withdraw_funds()
# Withdraw funds from customer1 savings account
account3.set_withdraw_funds()
account3.get_overview()
print("Number of current accounts: " + str(Current.number_of_current_accounts))
print("Number of savings accounts: " + str(Savings.number_of_saving_accounts))
