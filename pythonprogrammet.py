print(900 * 2 * 1.25 + 100 * 1.06)

robot_price = 900
robot_amount = 2
robot_tax = 1.25
book_prize = 100
book_amount = 1
book_tax = 1.06

print(robot_price * robot_amount * 
	robot_tax + book_prize * book_amount * book_tax)

robot = {"price": 900, "amount": 2, "tax": 1.25}
book = {"price": 100, "amount": 1, "tax": 1.06}

print (robot["price"] * robot["amount"] * robot["tax"] + book["price"] * 
	book["amount"] * book["tax"])

class Product:
	price = 0
	amount = 0
	tax = 0 
	def price_with_tax(self):
		return self.price * self.amount * self.tax 

robot = Product()
robot.price = 900
robot.amount = 2
robot.tax = 1.25 
robot.total = 900 * 2 * 1.25

book = Product()
book.price = 100
book.amount = 1
book.tax = 1.06
book.total = 100 * 1 * 1.06

print(robot.total + book.total)



print(book.price_with_tax() + robot.price_with_tax())

class Product:
	def __init__(self, price, amount, tax, name):
		self.price = price
		self.amount = amount
		self.tax = tax
		self.name = name 
	def price_with_tax(self):
		return self.price * self.amount * self.tax
	def price_with_tax_discount(self):
		total = self.price * self.amount * self.tax 
		if total > 500:
			return 0.9 * total
		else:
			return total 

robot = Product(price=900, amount=2, tax=1.25, name="robot")
book = Product(price=100, amount=1, tax=1.06, name="bok")
computer = Product(price=1000, amount=1, tax=1.25, name="dator")

print(robot.price_with_tax() + book.price_with_tax() + computer.price_with_tax())

products = [robot, book, computer]
total_price = 0
for product in products:
	total_price += product.price_with_tax()
print(total_price)
for product in products:
	print(product.name, product.price_with_tax())
for product in products: 
	print(product.name, product.price_with_tax_discount())

