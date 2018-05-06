class BankAccount():
	__no_of_accounts = 0

	def __init__(self,name,balance):
		if name != []:
			self.__name = name
			print("A bank account for",name,"is open.")
			BankAccount.__no_of_accounts += 1
		if balance >= 0: 
			self.__balance = balance
			print("Your current balance is",balance,"won")
		else:
			self.__balance = 0
			print("Your current balance is",balance,"won")

	def __str__(self):
		print(self.__name + "'s BankAccount object")

	def show__balance(self):
		print(self.__name + "'s balance is 70000 won.")

	def deposit(self,amount):
		if int(amount) > 0:
			self.__balance += int(amount)
			print(amount,"won has been successfully deposited.")
			print(self.__name + "'s balance is",self.__balance,"won.")
		else:
			print("Deposit failed.")
			print(self.__name + "'s balance is",self.__balance,"won.")

	def withdraw(self,amount):
		if int(amount) >= 0 and int(amount) <= self.__balance:
			self.__balance -= int(amount)
			print(self.__balance,"won has been successfully withdrawn.")
			print(self.__name,"'s balance is",self.__balance,"won.")
		else:
			print("Withdraw failed")
			print(self.__name,"'s balance is",self.__balance,"won.")

	@staticmethod 
	def count_accounts(): 
		return BankAccount.__no_of_accounts
	



		