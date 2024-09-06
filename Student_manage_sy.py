# student registration
# add data
# update data
# delete data
# search
# filter
db1 = {101:{"name":"gaurav", "course":"python", "city":"pune", "per":23}}
print("_"*150,"\n")
print("Student Registration System".center(150))
print("_"*150)
while True:
        print("""
                            Dashboard
        
        1.Add student Detail      2.Display student Details
        3.Updated student details  4.Delete studetn details
        5.Search student detil    6.Filter
        7.Break

        """)

        ch = int(input("Enter Your Choice: "))
        if ch == 1:
            reg = eval(input("Enter the registration numb: "))
            name = input("Enter the name: ")
            city = input("Enter  the city: ")
            per = int(input("Entet the per :"))
            course = input("Ener thec course: ")
            db1[reg] = {"name":name, "city":city, "per":per, "course":course}
            print("Added Succefully")
        
        elif ch == 2:
            print("_"*100)
            print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}".format("reg","name","city","per","course"))
            print("_"*100)
            for i in db1:
        
                print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}".format(i,db1[i]["name"],db1[i]["city"],db1[i]["per"], db1[i]["course"]))
                print("_"*100)
            
        elif ch == 3:
            reg = eval(input("Enter Registration Number: "))
            print("""
            1.Name      2.City
            3.per`      4.course
            """)
            ch = eval(input("Enter You choice: "))
            if ch == 1:
                uname = input("Enter the Name :")
                db1[reg]["name"] = uname
                print("Updated Succefully")
            elif ch == 2:
                uname = input("Enter the UserName: ")
                db1[reg]["city"] = uname
                print("succefully updated")
            elif ch == 3:
                uname = input("Enter the Name :")
                db1[reg]["per"] = uname
                print("Updated Succefully")
            elif ch == 4:
                uname = input("Enter the Name :")
                db1[reg]["course"] = uname
                print("Updated Succefully")
            else:
                print("invalid")
        elif ch == 4:
            print("_"*90)
            reg = int(input("Enter the registration number :"))
            #db1.pop(reg)
            del db1[reg]
            print("_"*90)
        elif ch == 5:
            
            print("""
            1.Name      2.City
            3.per`      4.course
            """)
            ch = int(input("Enyer the choice: "))
            if ch == 1:
                print("_"*100)
                print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}".format("reg","name","city","per","course"))
                print("_"*100)
                name = input("Enter the name :")
                for i in db1:
                    if db1[i]["name"] == name:
                        print("_"*100)    
                        print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}".format(i,db1[i]["name"],db1[i]["city"],db1[i]["per"], db1[i]["course"]))
                        print("_"*100)
                
        elif ch == 6:
            break
        else:
            print("Invalid")

# Interview questions
# create a project -> Employee Managegemt system
# ATM
