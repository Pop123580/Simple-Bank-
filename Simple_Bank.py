'''
def greet(name="friend"):
    print(f"Hello,{name}!")

greet("Alice")
greet()  
'''

'''
def calculation(a,b):
    return a/b,a*b,a+b,a-b
DMAS=calculation((int(input("Enter first number: "))),int(input("Enter second number: ")))
print("DMAS: ",DMAS)
'''


'''
def square(a):
    return a**2

result=square(int(input("Enter a number: ")))
print("Square result:", result)
'''
# __________________________________________________________________________________________________________________

print("Welcome to Goku Bank")
balance = 0.0
attempts = 0
correct_pin=9522
while True:
    
    pin=int(input("Enter your pin: "))
    attempts += 1
    if attempts > 3:
        print("Too many attempts, exiting.")
        exit()
    if pin==correct_pin:
        print("Pin is correct")
        break
    else:
        print("Incorrect pin, try again")
while True:
    def deposit(balance,amount):
        return balance+amount

    def withdarw(balance,amount):
        if amount > balance:
            print("bsdk paise to daal le")
            return balance
        else:
            return balance-amount
    
    def check_balance(balance):
        return balance

   
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4.Exit")

    choice=int(input("Enter your choice: "))
   
    if choice ==1:
        amount=float(input("Enter amount to depodit: "))
        balance=deposit(balance,amount)

    elif choice ==2:
        amount=float(input("Enter amount to withdraw: "))
        balance=withdarw(balance,amount)

    elif choice ==3:
        print("Your balance is:", check_balance(balance))
        if balance < 0:
            print("Your balance is negative, please deposit money to avoid penalties.")
    
    elif choice ==4:
        print("Thankyou for your visit")
        break
    
    else:
        print("Invlid choice")

