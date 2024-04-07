import random
class Bank:
    def __init__(self):
        self.client_detail_list=[]
        self.loggedin=False
        self.cash=0
        self.Transfercash=False

#Register
    def register(self,name,phone,password):
        cash=self.cash
        conditons=True
        if len(str(phone))<10 or len(str(phone))>11:
            conditons=False
            print("Invalid phone Number")
        if len(str(password))<5 or len(str(password))>18:
            conditons=False
            print("Enter password phone Numberm between 6 to 17 digit")
        if conditons==True:
            random_number = random.randint(100000000000, 999999999999)
            print("Your Bank Account Number:",random_number)
            print("Account Created Sucessfully")
            
            self.client_detail_list=[name,phone,password,cash,random_number]
            with open(f"{name}.txt","w") as f:
                for details in self.client_detail_list:
                    f.write(str(details)+"\n")
#login functon
    def login(self,name,phone,password):
        with open(f"{name}.txt","r") as f:
            details=f.read()
            self.client_detail_list=details.split("\n")
            if str(phone) in str(self.client_detail_list):
                if str(password) in str(self.client_detail_list):
                    self.loggedin=True
            if self.loggedin==True:
                print(f"{name},logedin sucessfully")
                self.cash=int(self.client_detail_list[3])
                self.name=name
            else:
                print("Wrong Details,Your detials are not valid")
# Add cash
    def add_cash(self,amount):
        if amount>0:
            self.cash+=amount
            with open(f"{name}.txt","r") as f:
                details=f.read()
                self.client_detail_list=details.split("\n")
            with open(f"{name}.txt","w") as f:
                f.write(details.replace(str(self.client_detail_list[3]),str(self.cash)))
            print("Added amount sucessfully")
        else:
            print("Enter correct value of amount")
# Transfercash
    def Transfer_cash(self,amount,name,phone):
        with open(f"{name}.txt","r") as f:
            details=f.read()
            self.client_detail_list=details.split("\n")
            if str(phone) in self.client_detail_list:
                self.Transfercash=True

        if self.Transfercash==True:
            total_cash=int(self.client_detail_list[3])+amount
            left_cash=self.cash-amount

            with open(f"{name}.txt","w") as f:
                f.write(details.replace(str(self.client_detail_list[3]),str(total_cash)))
            with open(f"{name}.txt","r") as f:
                details_2=f.read()
                self.client_detail_list=details_2.split("\n")
            with open(f"{self.name}.txt","w")as f:
                f.write(details_2.replace(str(self.client_detail_list[3]),str(left_cash)))
            print("Amount Transferred Sucessfully to",name,"-",phone)
            print("Balance left in Account=",left_cash)
            print("-----------------------")
            self.cash=left_cash
#Edit Phone and password
    def password_change(self,password):
        if len(str(password))<5 or len(str(password))>18:
            print("Enter the password greater then 5 and smaller than 18")
        else:
            with open(f"{self.name}.txt","r") as f:
                details=f.read()
                self.client_detail_list=details.split("\n")
            with open(f"{self.name}.txt","w") as f:
                f.write(details.replace(str(self.client_detail_list[2]),str(password)))
                print("Password is updated Suceesfully")
    def phone_change(self,phone):
        if len(str(phone))<10 or len(str(phone))>11:
            print("Invalid phone number!")
        else:
            with open(f"{self.name}.txt","r") as f:
                details=f.read()
                self.client_detail_list=details.split("\n")
            with open(f"{self.name}.txt","w") as f:
                f.write(details.replace(str(self.client_detail_list[1]),str(phone)))
                print("New phone Number setup suceesfully")

if __name__== "__main__":
    Bank_obj=Bank()
    print("----------------------")
    print("welcome to My Bank")
    print("----------------------")
    print("1.Login")
    print("2.Create a New Account")
    user=int(input("Enter a Choice:"))
    if user==1:
        print("Logging in")
        name=input("Enter Name:")
        phone=int(input("Enter phone:"))
        password=input("Enter Password:")
        Bank_obj.login(name,phone,password)
        while True:
            if Bank_obj.loggedin == True:
                print("Enter your Choice")
                print("----------------------")
                print("1.Add amount")
                print("2.Check balance")
                print("3.Transfer Amount")
                print("4.Edit Profile")
                print("5.Logout")
                print("----------------------")
                login_user=int(input())
                if login_user==1:
                    amount=int(input("Enter amount"))
                    Bank_obj.add_cash(amount)
                    print("----------------------")
                    print("\n1.Back menu")
                    print("\n2.Logout")
                    print("----------------------")
                    choose=int(input())
                    if choose==1:
                        continue
                    if choose==2:
                        print("Logout Successfully!")
                        break
                if login_user==2:
                    print("Current Balance=",Bank_obj.cash)
                    print("--------------------------")
                    print("\n1.Back Menu")
                    print("\n2.logout")
                    choose=int(input())
                    if choose==1:
                        continue
                    if choose==2:
                        break
            if login_user==3:
                print("Balance=",Bank_obj.cash)
                amount=int(input("enter amount"))
                if amount>=0 and amount<=Bank_obj.cash:
                    name=input("Enter Person Name:")
                    phone=input("Enter Person Phone Number")
                    Bank_obj.Transfer_cash(amount,name,phone)
                    print("\n1.Back Menu")
                    print("\n2.logout")
                    choose=int(input())
                    if choose==1:
                        continue
                    if choose==2:
                        print("Logout Successfully!")
                        break
                elif amount<0:
                    print("Enter please correct value of amount")
                elif amount>Bank_obj.cash:
                    print("Insufficient Balance")
            if login_user==5:
                print("Logout Sucessfully")
                break
            if login_user==4:
                print("1.Password Change")
                print("2.Phone Number Change")
                edit_profile=int(input())
                if edit_profile==1:
                    new_password=input("Enter New Password")
                    Bank_obj.password_change(new_password)
                  
                    print("\n1.Back Menu")
                    print("\n2.Logout")
                    choose=int(input())
                    if choose==1:
                        continue
                    if choose==2:
                        print("Logout Successfully!")
                        break
                elif edit_profile ==2:
                    new_phone=int(input("Enter New Phone Number"))
                    Bank_obj.phone_change(new_phone)
                
                    print("\n1.Back Menu")
                    print("\n2.Logout")
                    choose=int(input())
                    if choose==1:
                        continue
                    if choose==2:
                        print("Logout Successfully!")
                        break

                
    if user==2:
        print("Creating a New Account")
        name=input("Enter Name:")
        phone=int(input("Enter Phone Number:"))
        password=input("Enter Password:")
        Bank_obj.register(name,phone,password)
        print("\n1. Press 1 for Exit")
        choose=int(input())
        while True:
            if choose==1:
             print("Exit Successfully!")
             break
        
        







        





    
    

                








