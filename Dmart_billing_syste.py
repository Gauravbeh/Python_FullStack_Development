print("_"*100,"\n")
print("\t\t\t\tD-Mart Billing System")
print("_"*100)

db1 = {1:"Cloth", 2:"shoes", 3:"food", 4:"Aata"}
db2 = {1:50, 2:40, 3:30, 4:20}
db3 = {1:20, 2:15, 3:10, 4:5}

itemkey = []
qunt = []

while True:

    print(f"""
                    Menus
        1.cloth                2.shoes
        3.food                 4.Aata

        {'_'*150}      
    """)
    item = eval(input("Enter the choice: "))
    quantiy = eval(input("Enter the quantity: "))
    itemkey.append(item)
    qunt.append(quantiy)

    dc = input("Do you want to continue y/n :").lower()
    if dc == 'n':
        print("_"*110)
        #print("|{:^20}|{:^20}|{:^20}|{:^20}".format("item","quantity","price","amount","discount"))
        print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("item","qunatity","price","Discount","amount"))
        print("_"*110)

        
        for i in range(len(itemkey)):
            disc = (qunt[i]*db2[itemkey[i]] *db3[itemkey[i]]) / 100
            print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}".format(db1[itemkey[i]],qunt[i], db2[itemkey[i]],db3[itemkey[i]],qunt[i]*db2[itemkey[i]]-disc))
            
            
        break
