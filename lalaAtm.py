a=12345
b=4444
z=10000
def lalaAtm():


    
    c=int(input("Enter ac number: "))
    d=int(input("enter pin: "))
    #creating funtion to perform variou task o the atm
    def withdraw():
        f=int(input("Enter amont: $" ))
        if f>=z:
            print("insufficient funds")
        elif f<z and f>=10:
            print("withdraw cash")
        else :
            print("invalid input!")

    def balance ():
        print("$",z)

    def deposit ():
        g=int(input("Enter amont: $"))
        print("insert  $",g)
        print("New available bal: $",z)


    if a==c and b==d:
        print("WELCOM TO LALA BANK")
        print("1.withdraw\n2.balance check\n3.deposit")


        e=int(input("choose task from 1-3:"))
        if e==1:
            withdraw()
        elif e==2:
            balance()
        elif e==3:
            deposit()

        else:
            print("error invalid input!")
    else:
        print("error invalid input!")
    
while 1<2:
    lalaAtm()
