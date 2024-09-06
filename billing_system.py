db1 ={1:"poha", 2:"samosa", 3:"Tea", 4:"Vadapav", 5:"Idali", 6:"Cofee"}
db2 = {1:20, 2:15, 3:12, 4:15, 5:30, 6:25}
itemkey = []
sq = []

print("_"*150,"\n")
print("\t\t\t\t\t\t\t\t Garva Hotel ")
#print(f"{''*80}Garva Hotel")
print("_"*150)
while True:
    print(f"""
                    Menus
        1.Poha                2.Samosa
        3.Tea                 4.Vadapav
        5.Idali               6.Cofee  

        {'_'*150}      
    """)
    item = eval(input("Enter Your Choice: "))
    quantity = eval(input("Enter the Quantity: "))
    itemkey.append(item)
    sq.append(quantity)
   
    ch = input("Do you want to Continue(y/n): ").lower()
  
    if ch == 'n':
        print("_"*85)
        print("|{:^20}|{:^20}|{:^20}|{:^20}".format("item","quantity","price","amount"))
        print("_"*85)
        sum =0
        for i in range(len(itemkey)):
            print("|{:^20}|{:^20}|{:^20}|{:^20}".format(db1[itemkey[i]],sq[i], db2[itemkey[i]],sq[i]*db2[itemkey[i]]))
            sum = sum + sq[i]*db2[itemkey[i]]
            print("_"*85)
        print("The total amount is: ",sum)
        break
    
  
     

# changes = error 8
# Assingment for Interview Questinos :->

# Create project
#1.Create Project
#Dmart billing system and discount