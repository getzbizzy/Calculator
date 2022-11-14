import art

def add(n1, n2):
  return n1 + n2
def subtract(n1, n2):
  return n1 - n2
def multiply(n1, n2):
  return n1 * n2
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator():
  print(art.logo)
  num1 = float(input("What's the first number? "))
  for symbol in operations:
    print(symbol)
  operator = input("Pick an operator from the list above: ")
  num2 = float(input("What's the second number? "))
  calculation_function = operations[operator]
  answer = calculation_function(num1, num2)
  print(f"{num1} {operator} {num2} = {answer}")
  keep_calculating = input(f"Type 'y' if you want to keep calculating with {answer}, or  type 'n' to clear the calculator: ")
  previous_answer = answer
  if keep_calculating != "y":
      calculator()

  while keep_calculating == "y":
    operator = input("Pick an operator: ")
    num_next = float(input("What's the next number? "))
    calculation_function = operations[operator]
    next_answer = calculation_function(previous_answer, num_next)
    print(f"{previous_answer} {operator} {num_next} = {next_answer}")
    keep_calculating = input(f"Type 'y' if you want to keep calculating with {next_answer}, or  type 'n' to clear the calculator: ")
    previous_answer = next_answer
    if keep_calculating != "y":
      calculator()
calculator()