def greet_welcome():
    print("Welcome to Python functions")

greet_welcome()

def greet_different():
    print("Hello! This is a different greeting.")

greet_different()
greet_different()

def greet_user(name):
    print("Hello", name)

greet_user("Navi")

def show_double(number):
    print("Double of", number, "is", number * 2)

show_double(6)
show_double(9)

def display_total(price, quantity):
    print("Total:", price * quantity)

display_total(5,3)

def show_remaining(budget, spent):
    print("Remaining budget:", budget - spent)

show_remaining(100, 35)

def calculate_total(price, quantity):
    return price * quantity
total = calculate_total(5, 3)
print("Total:", total)

def calculate_tax(price, tax_rate):
    return price * tax_rate
tax = calculate_tax(250, 0.08)
final_price = 250 + tax
print("Tax:", tax)
print("Final price:", final_price)


def check_result(score):
   if score >= 60:
       return "Pass"
   else:
       return "Fail"

result = check_result(45)

print("Result:", result)

def check_access(age, has_id):

    if age >=18 and has_id == True:
        return "Access granted"
    else:
        return "Access denied"
    
access = check_access(20, False)

print("Access:", access)