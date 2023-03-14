from accounts.accounts import Account


# inheritance
class Savings(Account):

    # class variable
    number_of_saving_accounts = 0

    # constructor
    def __init__(self, savings_id, savings_type, savings_balance, savings_interest_rate, cust_obj):
        # calling the super class constructor
        super().__init__(savings_id, savings_type, savings_balance, cust_obj)
        self._interest_rate = savings_interest_rate
        Savings.number_of_saving_accounts += 1
