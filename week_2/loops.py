# ****** loops ******


# for loop example
def for_loop():
    for i in range(5):
        print(i, end=" ")
    print("done!")


# 'continue' example
def delete_spaces(sen):
    sen_no_spaces = ""
    for c in sen:
        if c.isspace():
            continue
        sen_no_spaces += c
    print(sen_no_spaces)


# 'break' example
def is_string_contain_num(is_number):
    for c in is_number:
        if c.isdigit():
            print("A number was found:", c)
            break
        else:
            print("Found '" + c + "' which is not a number!")


# while loop example
def while_loop():
    i = 0
    while i < 5:
        print(i, end=" ")
        i += 1
    print("done!")


# for vs while
# Greatest common divisor(GCD) of two numbers - naive version
def gcd_for_loop():
    a = int(input("Please insert number: "))
    b = int(input("Please insert number: "))
    for r in range(a, 0, -1):
        if a % r == 0 and b % r == 0:
            break
    print("The GCD of", a, "and", b, "is", r)


# Greatest common divisor(GCD) of two numbers - Euclidean Algorithm
def gcd_while_loop():
    a = int(input("Please insert the first number: "))
    b = int(input("Please insert the second number: "))
    j = a
    i = b
    while i != 0:
        reminder = j % i
        j = i
        i = reminder
    print("The GCD of", a, "and", b, "is", j)


if __name__ == '__main__':
    for_loop()
    delete_spaces("Ground control to major Tom")
    is_string_contain_num("ab4cde")
    while_loop()
    gcd_for_loop()
    gcd_while_loop()
