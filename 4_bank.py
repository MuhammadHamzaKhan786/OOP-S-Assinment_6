class Bank:
    bank_name = "HBL Bank"
    bank_name1 = "Faysal Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    @classmethod
    def change_bank_name1(cls, name):
        cls.bank_name1 = name

if __name__ == "__main__":
    user1 = Bank()
    user2 = Bank()

    print("Before changing bank names:")
    print(f"User1's bank_name: {user1.bank_name}")
    print(f"User2's bank_name1: {user2.bank_name1}")


    Bank.change_bank_name("UBL Bank")
    Bank.change_bank_name1("MCB Bank")

    print("\nAfter changing bank names:")
    print(f"User1's bank_name: {user1.bank_name}")
    print(f"User2's bank_name1: {user2.bank_name1}")
