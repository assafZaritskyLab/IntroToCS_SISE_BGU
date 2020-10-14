# ****** Conditional statements ******

# Example-1: Determine weather two numbers have the same reminder by 7:
# if statement
def if_statement():
    a = int(input("Please insert an integer number: "))
    b = int(input("Please insert another integer number: "))
    if a % 7 == b % 7:  # compare between the reminders
        print("The numbers have the same reminder by 7")


# if-else statement
def if_else_statement():
    a = int(input("Please insert an integer number: "))
    b = int(input("Please insert another integer number: "))
    if a % 7 == b % 7: # compare between the reminders
        print("The numbers have the same reminder by 7")
    else:
        print("The numbers have different reminders by 7")


# Example-2: Classify the type of triangle from given 3 sides lengths.
# if-elif-else statement
def if_elif_else_statement():
    a = int(input("Please insert the first side: "))
    b = int(input("Please insert the second side: "))
    c = int(input("Please insert the third side: "))

    if a == b == c:  # There are all equal
        print("Equilateral triangle")
    elif a == b or a == c or b == c:  # only two equal
        print("Isosceles triangle")
    else:  # all three sides have different lengths
        print("Scalene triangle")


# Example-3: Check if number is divisible by 2, 5 or none of them.
# nested conditional statement
def nested_conditional_statement():
    n = int(input("Please insert an integer number: "))
    if n % 2 == 0:
        if n % 5 == 0:  # NESTED if
            print(n, 'is divisible by 2 and by 5, so also by 10.')
        else:  # NESTED else, pertains to NESTED if.
            print(n, 'is divisible by 2 but not by 5.')
    elif n % 5:
        print(n, 'is divisible by 5 but not by 2.')
    else:
        print(n, 'is not divisible by 2 and 5.')


if __name__ == '__main__':
    if_statement()
    if_else_statement()
    if_elif_else_statement()
    nested_conditional_statement()
