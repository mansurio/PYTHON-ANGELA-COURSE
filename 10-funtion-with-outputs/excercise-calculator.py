# def add(n1, n2):
#     return n1 + n2
#
#
# def subtract(n1, n2):
#     return n1 - n2
#
#
# def multiply(n1, n2):
#     return n1 * n2
#
#
# def divide(n1, n2):
#     return n1 / n2
#
#
# print(add(2, multiply(5, divide(8, 4))))

# def out_func(a, b):
#     def in_fuc(c, d):
#         return c + d
#
#     return in_fuc(a , b)
#
#
# result = out_func(5, 10)
# print(result)

# todo -- CALCULATOR --
# ADD
def add(n1, n2):
    return n1 + n2


# SUBSTRACK
def substrac(n1, n2):
    return n1 - n2


# MULTIPLY
def multyplay(n1, n2):
    return n1 * n2


# DIVIDE
def divide(n1, n2):
    return n1 / n2


operation = {"+": add, "-": substrac, "*": multyplay, "/": divide}

num1 = int(input("Whats the first number...?"))
num2 = int(input("Whats the second number...?"))

for simbol in operation:
    print(simbol)

ope_symbol = input("Pic the operator from the line above...:")
calck_simbol = operation[ope_symbol]
answer = calck_simbol(num1, num2)
print(f" {num1} {ope_symbol} {num2} = {answer}")
