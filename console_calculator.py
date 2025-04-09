"""
This module is the simple console calculator which saves calculation history to the file
"""


OPERATORS = {
	'+': lambda a, b: a + b,
	'-': lambda a, b: a - b,
	'*': lambda a, b: a * b,
	'/': lambda a, b: a / b,
	'**': lambda a, b: a ** b,
	'%': lambda a, b: a % b
}


def calculate(a, operator, b):
	"""
	calculates value of a, b using OPERATORS dictionary for operators as keys and lambda functions as values
	"""
	return OPERATORS[operator](a, b)


def user_expression():
	"""
	Takes user input, splits it into variables, checks for the valid operator
	"""
	global res
	while True:
		try:
			if not res:
				user_expr = input("Enter expression (for example, 2 + 3): ")
				a, operator, b = user_expr.split()	
			else:
				user_expr = input(f"Enter expression (for example, + 5). Current value: {res} -> ")
				operator, b = user_expr.split()
				a = res
			if operator in OPERATORS:
				break
			print(f"Unsupported operator: {operator}")
		except ValueError:
			if not res:
				print("Invalid input: expected format 'a + b'")
			else:
				print("Invalid input: expected format '+ b'")
			write_to_file("Invalid input", "Error")
	return a, operator, b


def result(a, operator, b):
	"""
	Uses user input as an argument for the calculate() function
	"""
	global res
	while True:
		try:
			res = calculate(float(a), operator, float(b))
			expression = f"{a} {operator} {b}"
			print(f"Result: {res}")
			write_to_file(expression, res)
			break
		except ZeroDivisionError:
			print('Zero division is impossible')
			write_to_file("Attempt to divide by zero", "Error")
		except ValueError:
			print('Invalid input: only numbers and operator symbols are accepted( +, -, *, /, **, %)')
			write_to_file("Invalid input", "Error")


def write_to_file(expression, result):
	"""
	Writes user input and results to the "calculations_history.txt" file
	"""
	with open(f"calculations_history.txt", "a") as file:
		file.write(f"{expression} = {result}\n")


def main():
	"""
	Main function. Starts result() function with user_expression() function as an *args. Asks user for operation continue
	"""
	global res
	result(*user_expression())
	rep = input("Continue operations? (y/n): ").lower()
	if rep == 'y':
		main()
	else:
		res = 0
		print("Calculation finished")


if __name__ == "__main__":
	res = 0
	main()
