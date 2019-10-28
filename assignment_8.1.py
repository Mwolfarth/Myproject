class BankAccount:
	def _initl_(self, num, bal):
		self.accountNumber= num
		self.balance = float (bal)
		print ("A prepaid account has been created.")
		print("Your account number is" + str(self.accountNumber))
		print("Your balance is $" + str(self.balance))
	def withdrawl(self):
		withdrawlAmt= input("How much would you like to withdrawl?")
		self.balance= self.balance - float(withdrawlAmt)
		self.getBalance()
	def deposit (self):
		depositAmt= input("How much would you like to deposit?")
		self.balance= self.balance + float(depositAmt)
		self.getBalance()
	def getBalance(self):
		print("Your current account balance is: $" + str(self.balance))
class CheckingAccount (BankAccount):
	def _init_ (slef, num, bal, fee, minBalance):
		fees=5.00 
		minBal= 50.00
		BankAccount._init_(self, num, bal)
		self.accountFees= fees
		self.minimumBalance= minBal
		print("This account is a prepaid account.")
		print("The account fee is $" + str(self.accountFees))
		print("The minimun balance is $" + str(self.minimumBalance))
	def deductFees(self):
		self.balance= self.balance - self.accountFees
		print("Account fee in the amount of $" + str(self.accountFees) + "has been deducted.")
		self.getBalance()
	def checkMinBalance(self):
		Print("Checking if account balance meets the minimum balance requirement.")
		if self.balance >= self.minimumBalance:
			print("Account balance meets minimum balance requirement.")
		else:
			print("Account balance does not meet the minimum amount of: $" + str(self.minimumBalance))
			print("Please deposit more funds.")
class SavingsAccount (BankAccount):
	def _init_(self, num, bal,interestRate):
		interest_rate= 0.02
		BankAccount._init_(self, num, bal)
		self.accountRate=interest_rate
		print("This account is a prepaid account.")
		print("The account interest rate is $" + str(self.accountRate))
	def addInterest(self):
		self.balance = (self.balance * self.accountRate) + self.balance
		print("Interest rate was added.")
		self.getBalance()
print("Welcome to the Banking Program.")
try:
	flag1=0
	while flag1==0:
		print("")
		print("--Main Menu--")
		print("To open a prepaid account, press 1")
		print("To exit the programm, press 2")
		loop1= input("")
		
		if loop1 == '1':
			flag2=0
			while flag2==0:
				print("")
				print("__Account Creation--")
				print("A prepaid account has been created")
				print("Minimum balance is $50.00")
				print("Account Fees are $5.00")
				checkingAccountNumber= input("Enter an Account Number:")
				checkingAccountBalance= input("Enter Account Balance: $")
				my_CheckingAccount= CheckingAccount(checkingAccountNumber, checkingAccountBalance)
				my_CheckingAccount.checkMinBalance()
			
			flag3=0
			while flag3 == 0:
				print("")
				print("--My Acount--")
				print("What would you like to do?")
				print("To make a deposit, press 1")
				print("To make a withdrawl, press 2")
				print("To check balance, press 3")
				print("To return to the main menu, press 4")
				loop2= input("")
				
				if loop3== '1':
					my_checkingAccount.deposit()
				elif loop3 =='2':
					my_checkingAccount.withdrawl()
				elif loop3 =='3':
					my_checkingAccount.getBalance()
				elif loop4 =='4':
					print("Exiting to Main Menu")
					flag3=1
				else:
					print("Input not recognized")
		elif loop1 == '2':
			break
		else:
			print("Input not recognized")
