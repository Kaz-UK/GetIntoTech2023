from users.person import Person


# inheritance
class Employee(Person):

    # class variable
    number_of_employees = 0

    # constructor
    def __init__(self, employee_surname, employee_forenames, employee_address, employee_dob, employee_ni, employee_id,
                 employee_title, employee_salary):
        # calling the super class constructor
        super().__init__(employee_surname, employee_forenames, employee_address, employee_dob, employee_ni, employee_id)
        # construct items that only apply to employees
        self._title = employee_title
        self._salary = employee_salary
        # keep a number of total employees
        Employee.number_of_employees += 1

    def get_employee_name(self):
        print(self._forenames, self._surname, self._title)

    def get_employee_salary(self):
        print("Current salary is:", self._salary)

    def set_employee_password(self):
        self._password = input("Please create a new employee password: ")

    def set_title(self, new_job_title):
        self._title = new_job_title

    def set_salary_increase(self, new_salary):
        self._salary = new_salary + self._salary
        print(f"{self._forenames} {self._surname} your new salary is £{self._salary}. "
              f"This is a raise of £{new_salary}.")
