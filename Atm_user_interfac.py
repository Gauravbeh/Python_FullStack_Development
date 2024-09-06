db1 = {2222:{"name":"gaurav","ACnum":9607549517, "balance":500}}

print("_"*100,"\n")
print("ATM User Interface".center(100))
print("_"*100)

while True:
    print("""
                    Dashboard
            1.Enter Name, Account num, Account type
            2.Deposit Money
            3.Show total balance
            4.Withdraw
            5.Exit
        """)
    ch = int(input("Enter your choice: ".lower()))
    if ch == 1:
        pin = int(input("Enter the pin number: "))
        cname = input("Enter the name: ")
        acn = int(input("Enter account number: "))
        bal = int(input("Enter the Balance: "))
        db1[pin] = {"name":cname, "accnum":acn, "balance":bal}
        print(db1)
    elif ch == 2:
        pin=int(input("Enter the pin number :"))
        if pin in db1:
            add = int(input("Enter the Deposit Money: "))
            db1[pin]['balance']+=add
            print(db1)
    elif ch == 3:
        pin=int(input("Enter the pin number :"))
        if pin in db1:
            add = int(input("Enter the Deposit Money: "))
            db1[pin]['balance']-=add
            print(db1)
    elif ch == 4:
        pass
    else:
        print("Invalid")