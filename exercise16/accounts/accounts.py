# super class
class Account:

    def __init__(self, account_id, account_type, account_balance, cust_obj):
        self._id = account_id
        self._type = account_type
        self._balance = account_balance
        self.cust_obj = cust_obj

    def get_overview(self):
        print(f"Customer name: {self.cust_obj.cust_data()}, Account type: {self._type}, Account number: "
              f"{self._id}, Account balance: {self._balance}")

    def get_balance(self):
        print(f"The balance in {self._type} account number: {self._id} is {self._balance}")

    def set_add_funds(self):
        amount = float(input(f"How much would you like to deposit in {self._type}: "))
        self._balance = self._balance + amount
        print(f"Thank you for depositing £{amount} in you {self._type} account, your new balance is: £{self._balance}")

    def set_withdraw_funds(self):
        amount = float(input(f"How much would you like to withdraw from {self._type}: "))
        balance_check = self._balance - amount
        if balance_check >= 0:
            self._balance = self._balance - amount
            print(f"You have withdrawn £{amount} from your {self._type} account, your new balance is: £{self._balance}")
        else:
            print(f"You do not have available funds in {self._type}. Your balance is {self._balance}")
