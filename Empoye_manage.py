db1 = {101:{"ename":"gaurav", "salary":2399, "city":"pune", "company":"tcs"}}

print("_"*100,"\n")
print("Employee Management System".center(100))
print("_"*100)
while True:
    print("""
                                Dashboard
            1.Add Employee                  2.Display Employee
            3.Update Employee               4.Delete Employee

    """)
    ch = int(input("Enter the choice: ".lower()))
    if ch == 1:
        reg = int(input("Enter the regisration num: "))
        ename = (input("Enter the ename: "))
        salary = int(input("Enter the salary: "))
        city = input("Enter the city: ")
        company = (input("Enter the company: "))
        db1[reg] = {"ename":ename, "salary":salary, "city":city, "company":company}
        print(db1[reg])
        print("succefully added")

    elif ch == 2:
        print("_"*100)
        print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("reg","ename","city","salary","company"))
        print("_"*100)

        for i in db1:
            print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(i,db1[i]["ename"],db1[i]["salary"],db1[i]["city"],db1[i]["company"]))
            print("_"*100)
        print("Display Succefully")
    elif ch == 3:
        reg = int(input("Enter the registration num: "))
        print("""
        1.Ename     2.Salary
        3.City      4.Company
        """)
        ch = int(input("Enter your choice: "))
        if ch == 1:
            uname = input("Enter the Ename: ")
            db1[reg]["ename"] = uname
            print("Updated Succefully")
        elif ch == 2:
            salary = int(input("Enter the salary: "))
            db1[reg]["salary"] = salary
            print("updated sucessfully")
        elif ch == 3:
            city = input("Enter the city: ")
            db1[reg]["city"] = city
            print("Sucessfully updated")
        elif ch == 4:
            company = input("Enter the company: ")
            db1[reg]["company"] = company
            print("Updated Succefully")
    elif ch == 4:
        reg = int(input("Enter the registration Num: "))
        db1.pop(reg)
        print("Delete Succefully")
    elif ch == 5:
        break
    else:
        print("Invalid")
