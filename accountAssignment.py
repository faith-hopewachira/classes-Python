# Deposit/Withdraw
class Account:
    def __init__(self, pin, owner_person,bank_id, over_draft):
        self.__pin = pin
        self.__balance = 50000
        self.owner_person = owner_person
        self.bank_id = bank_id
        self.min_bal = 1000
        self.over_draft = 2000
        self.my_list = []
   
    def with_draw(self,amount,pin):
        if pin == self.__pin:
            withdrawn = f"You have withdrawn {amount} and your balance is {self.__balance - amount}"
            self.my_list.append(amount)
            print(self.my_list)

    def deposit(self,amount_deposited):
        self.__balance += amount_deposited
        self.my_list.append(amount_deposited)
        print(self.my_list)

        

        # print(f"You have deposited {amount_deposited} and your account balance {self.__balance}")

    
    # View Account Details: Method to display the account owner's details and current balance.
    def display_details(self):
        print('Name:',self.owner_person)
        print('Balance:',self.__balance)

    
    # Change Account Owner: Method to update the account owner's information.
    def change_owner(self,owner, id_bank):
        self.owner_person = owner
        self.bank_id = id_bank
        print("Your new name is {owner} and your account balance is {}")

    
    # Showw statements
    def show_statements(self):
        print(self.my_list)

    # Interest Calculation: Method to calculate and apply interest to the balance.
    def apply_interest(self, interest_percentage):
        interest = interest_percentage * self.__balance
        print(interest)


    def minimum_balance(self):
        if(self.__balance < self.min_bal):
            print("Account closed")
        else:
            print("Accounts still exists")

    # Transfer Funds: Method to transfer funds from one account to another.
    def transfer_funds(self, sendee, amount_sent):
        if amount_sent < self.__balance:
            print("Insufficient funds")
        else:
            print(f"{amount_sent} is sent to {sendee}")



    # Set Overdraft Limit: Method to set an overdraft limit for the account.
    def put_overdraft(self, put_amount):
        if put_amount > self.over_draft:
            print(f"Amount is overdraft by {self.over_draft-put_amount}")
        else:
            print("Okay")

    def close_account(self):
        if self.__balance<=0:
            print("Account closed!")
        else:
            print("Account still active")

    # Transaction History: Method to retrieve the history of all transactions made on the account.
    def transaction_history(self):
        print(self.my_list)





        
     






        




