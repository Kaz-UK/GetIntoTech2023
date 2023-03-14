from accounts.accounts import Account


# inheritance
class Current(Account):

    # class variable
    number_of_current_accounts = 0

    # constructor
    def __init__(self, current_id, current_type, current_balance, current_overdraft, cust_obj):
        # calling the super class constructor
        super().__init__(current_id, current_type, current_balance, cust_obj)
        self._overdraft = current_overdraft
        Current.number_of_current_accounts += 1

    # Current account will permit customer to go into debit if their overdraft permits (this overrides Accounts)
    def set_withdraw_funds(self):
        amount = float(input(f"How much would you like to withdraw from {self._type}: "))
        balance_check = self._balance - amount
        if balance_check >= self._overdraft:
            self._balance = self._balance - amount
            print(f"You have withdrawn £{amount} from your {self._type} account, your new balance is: £{self._balance}")
        else:
            print(f"You do not have available funds in your {self._type} account. Your balance is {self._balance}")
