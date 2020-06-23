# from collections import namedtuple
#
#
# Habits = namedtuple('Habits', ('success', 'failure'))
# result = []
# for _ in range(5):
#     result.append()
#
#     # You are building an educational website and want to create a simple calculator for students to use. The calculator will only allow addition and subtraction of non-negative integers.
#
#     # We also want to allow parentheses in our input. Given an expression string using the "+", "-", "(", and ")" operators like "5+(16-2)", write a function to parse the string and evaluate the result.
#
#     # Sample output:
#     #   calculate("5+16-((9-6)-(4-2))+1") => 21
#     #   calculate("22+(2-4)") => 20
#     #   calculate("6+9-12") => 3
#     #   calculate("((1024))") => 1024
#     #   calculate("1+(2+3)-(4-5)+6") => 13
#     #   calculate("255") => 255
#
#     # n: length of the input string
#
#
#     import re
#
#
#     def calculator(expression):
#
#         result = 0
#         old_expression = expression
#         temp1 = expression.replace('+', " ")
#         temp2 = temp1.replace('-', " ")
#         numbers = temp2.split(" ")
#         index = 0
#         operators = []
#         for i in old_expression:
#             if i == '+' or i == '-':
#                 operators.append(i)
#
#         operators.insert(0, '+')
#         i = 0
#         while i < len(numbers):
#             op = operators.pop(0)
#             if op == '+':
#                 result += int(numbers[i])
#             elif op == '-':
#                 result -= int(numbers[i])
#             i += 1
#         return result
#
#
#     def calculator_with_braces(expression):
#
#         result = 0
#         old_expression = expression
#         temp1 = expression.replace('+', " ")
#         temp2 = temp1.replace('-', " ")
#         numbers = temp2.split(" ")
#
#         temp_expression=""
#         i = 0
#         stack  = []
#         while i <len(expression):
#             if expression[i] == "(":
#                 start = i+1
#                 while expression[i] != ")":
#                     if expression[i] == "(":
#                         stack.append(expression[start:i])
#                         start = 0
#                     i = i + 1
#
#                 end = i
#
#             calculator(expression[start:end])
#
#
#                 # print (calculator("255"))


def calculate(s):
    if not s: return 0
    s = "(" + s + ")"
    print s
    stack_num, stack_oper, cur_str = [], [], ""

    for i in range(len(s)):
        if s[i] == "+":
            stack_num.append(cur_str)
            stack_oper.append("+")
            cur_str = ""
        elif s[i] == "-":
            stack_num.append(cur_str)
            stack_oper.append("-")
            cur_str = ""
        elif s[i] == "(":
            stack_num.append("(")
            stack_oper.append("(")
            cur_str = ""
        elif s[i] == ")":
            stack_num.append(cur_str)
            cur_res = 0
            while stack_oper[-1] != "(":
                if stack_oper[-1] == "+":
                    cur_res += int(stack_num.pop())
                    stack_oper.pop()
                    print stack_oper
                elif stack_oper[-1] == "-":
                    cur_res -= int(stack_num.pop())
                    stack_oper.pop()
                    print stack_oper
            print stack_num
            cur_res += int(stack_num.pop())
            stack_num.pop()
            stack_oper.pop()
            print stack_num
            print stack_oper
            cur_str = str(cur_res)
        else:
            cur_str += s[i]

    return int(cur_str)

print calculate("22+(2-4)")