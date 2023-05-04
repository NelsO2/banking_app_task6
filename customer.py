
import random,math
import datetime
import sys
try:
    
    class Customer_Bank_account:
        """this is the blue print/prototype from where other customer account are created"""
        acc_num = ""

        def __init__(self):
            """this method let the class initialize the object attribute, is called every time a customer is created"""
            self.balance = 0
        
        def Create_acc(self):
            """user to be able to create account and also sign-up"""
            print("Please Enter your details to Proceed :")
            self.name =input('Enter Your Name : ').capitalize()
            self.email = input('Enter Your Email : ').casefold()            
            date_of_birth = input('Enter your birth date [dd/mm/yyyy] :  ')
            self.age = int(input('Enter Your Age : '))
            self.mobile_no = int(input('Enter your mobile no : '))
            account_num = self.randomNumber(10)
            print(f"Congratulation your Account created Successfully .... Your account number is={account_num}")
            self.acc_num = account_num
            print('-'*70)

            # user can choose either Saving or current account
            acc_type = input ("Enter which type of account do you want to open [savings/current] : ").casefold()
            if acc_type =='savings':
                print("MINIMUM BALANCE OF ₦500. FOR OPENING SAVINGS ACCOUNT") 
            elif acc_type =='current':
                print("MINIMUM BALANCE OF ₦5000. FOR OPENING CURRENT ACCOUNT")
            else:
                print('Invalid Input....Try again with available options')

            # instanciating acc_type attribute
            self.a_type =acc_type
            print('-'*70)
            opening_amt =float(input("Enter The Initial amount(>=₦500 for Saving and >=₦5000 for current : "))
            self.balance += opening_amt
            print('-'*70)

            # new user creating password
            pwd = input("Create strong password containig uppercase,lowercase ,symbol,and number in combination[Abc@123] = ")
            conf_pwd= input("Confirm Your Password = ")
            if conf_pwd == pwd:
                print("Registration Successful")


                with open("login_detail.txt", 'w') as f:
                    """writing / saving user email, password and account number to an external file called login_detail.txt"""
                    f.write(self.email + "\n")
                    f.write(pwd + "\n")
                    f.write(str(account_num))
                f.close()
            else:
                print("Password did not match! \n")
    

        def login(self):
            """Registered customer can login"""
            print('-'*50)
            print("*****LOGIN TO ENTER*****")
            print("-"*50)
            Email =input("enter your email address = ")
            password =input("enter your password = ")
            account_no = self.acc_num
            with open("login_detail.txt",'r') as f:
                """reading the registered customer email, password account number to log him/her in"""
                Save_Email, Save_password, save_account_no = f.read().split("\n")
                f.close()

                if Email == Save_Email and password ==Save_password : # statement to check whether the email and password is thesame as the in the login_detail.txt file
                  
                    print("\t\t\t****LOGGED IN SUCCESSFULLY**")
                    print('-'*50)
                    
                    while True:
                        """if any of the following condition is true, customer should be able to do any of the following transactions"""
                        print(f"\t MAIN MENU LIST \n \
                            \t1)VIEW ACCOUNT INFO \n \
                            \t2)DEPOSIT MONEY \n \
                            \t3)WITHDRAW MONEY \n \
                            \t4)VIEW TRANSACTION HISTORY \n \
                            \t5)DISPLAY BALANCE \n \
                            \t6)TRANSFER TO ANOTHER ACCOUNT \n \
                            \t7)EXIT")
                        # customer to select from available menu
                        choice = int(input("Pick an option [1/2/3/4/5/6/7]= "))
                        if choice == 1:
                            obj.Show_Acc_Info()
                            print(f"\t\t\t\tWelcome {self.name} ")
                            print('-'*70)
                        elif choice == 2:
                            obj.Deposit()
                            print("credit transaction occur in your account ...") 
                            print('-'*70)    
                        elif choice == 3:
                            obj.Withdrawal() 
                            print("Thank you...") 
                            print('-'*70)    
                        elif choice == 4:
                            print("your transaction history: ")
                            try: # to check for possible error(s)
                                with open('transactions.txt', 'a+',encoding='utf-8') as file:
                                    for line in (file.readlines()):
                                        print(line, end ='')
                            except Exception as ex:
                                print(f"Problem Occurred = {ex}")
                            print('-'*70)
                        elif choice == 5:
                            obj.DisplayBal()
                            print('-'*70)

                        elif choice == 3:
                            obj.transfer() 
                            print("Thank you...") 
                            print('-'*70)

                        elif choice == 7:
                            print("Thanks you, see you again")
                            sys.exit()
                        else:
                            print('input valid choice')
                else:
                    print("login failed try again")

        def randomNumber(self,n:int):
            min = math.pow(10,n-1)
            max = math.pow(10,n)-1
            self.n=n
            return random.randint(min,max)

        def Show_Acc_Info(self):
            print(f'\n 1]Account No : {self.acc_num}')
            print(f'\n 2]Account holder Name : {self.name}')
            print(f'\n 3]Email Id of Account holder : {self.email}')
            print(f'\n 4]Type Of Account  : {self.a_type}')
            print(f'\n 5]Balance of Account : {self.balance}')

        def Check_balance (self):
            print(f'Available Balance: {self.balance}')

        def Deposit(self):
            amt = float(input("Enter amount to be deposited : "))
            self.balance+=amt 
            print(f"{amt} credited successfully in your account {self.acc_num} \n \
                 available balance is {self.balance}") 
            self.view_history(f"Deposit : {amt} amount credited at {datetime.datetime.today().replace(microsecond=0)}") 

        def Withdrawal(self):
            amt = float(input("Enter amount to be withdraw : "))
            self.balance-=amt 
            print(f"₦{amt} debited successfully from your bank account {self.acc_num} \n \
                 available balance is {self.balance}") 
            self.view_history(f"Withdraw : ₦{amt} amount debited at {datetime.datetime.today().replace(microsecond=0)}")

        def view_history(self,trans):
            with open('transactions.txt',mode='w',encoding='utf-8') as file:
                file.write(f"{trans} \t\t\t Available Balance: {self.balance} \n")

        def transfer(self, balance):
             """To transfer to other bank account"""
             amt = float(input("Enter receiver account number : "))
             amt = float(input("Enter amount you want to transfer : "))
             self.balance-=amt 
             print(f"₦{amt} transfer to ... successful {self.acc_num} \n \
                 available balance is {self.balance}") 
             self.view_history(f"Transfer : ₦{amt} amount debited at {datetime.datetime.today().replace(microsecond=0)}")    
        
        def DisplayBal(self):
            """here is to display account balance"""
            print('Your updated balance is ₦: ',self.balance)
            with open('transactions.txt',mode='r',encoding='utf-8') as file:
                print(file.read()) # read the balance from transaction.txt file where all transaction are saved

    def bank():
         """function to welcome the user to the platform"""
         greeting = "Welcome to CHAMPION Bank"
         print(greeting.center(70,'*'))
         input("Press Enter To Continue : ")
                    
    if __name__=="__main__":
        """this function tells the interpreter that this is the main function"""
        obj = Customer_Bank_account() 
        bank()
        while True:
            """loop for user to select from available menu"""
            print("\tMENU LIST")
            print("\t1]. CREATE ACCOUNT")
            print("\t2]. LOGIN")
            print("\t3]. EXIT")
            chc = int(input("Enter your choice [1/2/3] = "))
            if chc ==1:
                obj.Create_acc()
                obj.Show_Acc_Info()
            elif chc ==2:
                obj.login()
            elif chc== 3:
                print("\nThank You! . . . .")
                sys.exit()
            else:
                print("Please Enter a Valid Choice !")

except Exception as ex:
    print(f"<<<ERROR>>>{ex}")

finally:
    print("Thank you for banking with us, see you again......")
    