from users.person import Person


# inheritance
class Customer(Person):

    # class variable
    number_of_customers = 0

    # constructor
    def __init__(self, customer_surname, customer_forenames, customer_address, customer_dob, customer_ni, customer_id,
                 customer_credit_check):
        # calling the super class constructor
        super().__init__(customer_surname, customer_forenames, customer_address, customer_dob, customer_ni,
                         customer_id,)
        self._credit_check = customer_credit_check
        # Keep a number of total customers
        Customer.number_of_customers += 1

    # Change the customers credit check status
    def set_credit_check(self):
        check = input("Credit check completed (Y/N): ")
        if check.upper() == "Y":
            self._credit_check = True

    # Display a customers credit check status
    def get_credit_check(self):
        if not self._credit_check:
            print(f"No credit check on file for {self._forenames} {self._surname}")
        else:
            print(f"Credit check completed for {self._forenames} {self._surname}")

    # A method to create an instance of customer object to use with the account class
    def cust_data(self):
        return f"{self._forenames} {self._surname}"
