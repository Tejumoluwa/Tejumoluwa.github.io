import re
def main():
    """
    main function
    
    """
    sender = Customer("uba", "2234567890", 200000, 5678, "08012345678")
    USSD = input("USSD: ").strip()
    if USSD == "*375#":
        print("""1: Check balance
2: Send money
3: Purchase airtime """)
        while True:
            services = input()
            if services == "1":
                sender.check_balance()
                break
            elif services == "2":
                receiver = Customer("zenith", "2290876542", 300000, 2345, "08097654324")
                sender.send_money(receiver)
            elif services == "3":
                sender.purchase_airtime()
                break
            else:
                print("Invalid input")
    else:
        print("Invalid USSD")

        
class Customer:
    def __init__(self, bank="", account_no="", balance="", password="", phone_number=""):
        self.bank = bank
        self.account_no = account_no
        self.balance = balance
        self.password = password
        self.phone_number = phone_number
    
    def check_balance(self):
        """
        Checks the balance of the customer

        """
        # Input sender's password
        input_password = int(input("Password: "))
        if input_password == self.password:
            print(f"Your balance is {self.balance}")
        else: 
            print("Incorrect password")

    def send_money(self, receiver):
        """
        Sends a specified amount to a receiver
        
        """
        # Input receiver's bank
        user_bank = input("Bank: ").lower().strip()
        if user_bank == receiver.bank:
            # Input receiver's account number
            input_account_nu = input("Account Number: ").strip()
            if input_account_nu == receiver.account_no:
                # Input sender's password
                input_password = int(input("Password: "))
                if input_password == self.password:
                    amount = int(input("Amount to be transfered: "))
                    if amount < self.balance:
                        self.balance -= amount
                        receiver.balance += amount
                        print("Transfer was successful")
                    else:
                        raise ValueError("Insufficient balance")
                else:
                    raise ValueError("Incorrect password")
            else:
                raise ValueError("Wrong Account number")
        else:
            raise ValueError("Transfer was unsuccesful")
    
    def purchase_airtime(self):
        """
        Purchases airtime either 
        for the user or for someone else
        """
        user_bank = input("Bank: ").lower().strip()
        if user_bank == self.bank:
            input_password = eval(input("Password: "))
            if input_password == self.password:
                airtime = eval(input("Airtime amount: "))
            else:
                raise ValueError("Incorrect Password")
        receiver = input("Type 1, if you are purchasing for yourself or 2, for someone else: ").strip()
        if receiver == "1":
            if airtime < self.balance:
                self.balance -= airtime
                print("You have succesfully recharged")
            else:
                raise ValueError("Insufficient balance")
        elif receiver == "2":
            input_phone_no = input("Phone number: ").strip()
            if len(input_phone_no) == 11 and re.search(r"^0(7-9)(0-1)[0-9]+$", input_phone_no):
                if airtime < self.balance:
                    self.balance -= airtime
                    print("You have succesfully recharged")
                else:
                    raise ValueError("Insufficient balance")
            else:
                raise ValueError("Invalid Phonenumber")
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()