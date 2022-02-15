class Category:

	def __init__(self, category):
		self.category = category #name
		self.ledger = [] #ledger
		self.total = 0 #used for total calculations
		self.withdraws = 0 #used for creating charts

	def __str__(self):
		object_print = self.category.center(30,'*')+"\n"
		for x in self.ledger:
			self.total += x["amount"] #calcs all

			#lengths
			length_desc = len(x["description"])
			length_am = len(str(int(x["amount"])))

			#write
			object_print += x["description"][:length_desc + (23-length_desc)] + (" " * (23-length_desc))
			
			object_print += (" "*(4-length_am)) + str(x["amount"])

			if type(x["amount"]) == type(10):
				object_print += ".00"

			object_print += "\n" #newline

		object_print += "Total: " + str(self.total)
		return object_print
		
	def deposit(self, amount, description = ""):
		self.ledger.append({"amount":amount, "description":description})

	def get_balance(self):
		amount_inside = 0
		for x in self.ledger:
			amount_inside += x["amount"]
		return amount_inside
	
	def check_funds(self, amount):
		amount_inside = self.get_balance()
		if amount_inside >= amount:
			return True
		else:
			return False
	
	def withdraw(self, amount, description = ""):
		check = self.check_funds(amount)
		if check:
			self.ledger.append({"amount":(-amount), "description":description})
			self.withdraws += amount
			return True
		else:
			return False

	
	def transfer(self, amount, budget_category):
		check = self.check_funds(amount)
		if check:
			self.ledger.append({"amount":(-amount), "description":"Transfer to " + budget_category.category})
			budget_category.deposit(amount, "Transfer from " + self.category)
			return True
		else:
			return False
	
	

def create_spend_chart(categories):
	bar_chart = "Percentage spent by category\n"
	names = []
	for x in categories: #extracts names
		names.append(x.category)

	total_all = 0
	percentages = []

	for x in categories: #takes everything spent
		total_all += x.withdraws

	for x in categories: #calculates percentages, while rounding them down to 10
		true_percent = (x.withdraws/total_all)*100
		rounded = int(true_percent/10) * 10
		percentages.append(rounded)

	#writing
	longest = len(sorted(names, key=len, reverse=True)[0]) #takes the length of longest category name

	for x in reversed(range(11)): #y axis and bars
		current_p = x*10 #y-coord
		bar_chart += " "*(3-len(str(current_p))) + str(current_p) + "| "
		
		for i in percentages:
			if i >= int(current_p):
				bar_chart += "o  "
			else:
				bar_chart += "   "
		
		bar_chart += "\n" #new_line
	
	#x-axis
	bar_chart += "    " + "-" + "---"*len(categories) + "\n"

	for x in range(longest):
		bar_chart += " "*5
		for i in names:
			if x <= len(i)-1:
				bar_chart += i[x] + "  "
			else:
				bar_chart += "   "
		
		if x < (longest-1):
			bar_chart += "\n"


	return bar_chart