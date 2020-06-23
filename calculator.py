def calculator(string):

    if len(string) == 0:
        return 0

    stack, num, sign = [], 0, "+"

    for i in xrange(len(string)):
        if string[i].isdigit():
            num = num*10 + ord(string[i]) - ord("0")
        if (not string[i].isdigit() and not string[i].isspace()) or i == len(string) - 1:
            if sign == "-":
                stack.append(-num)

            elif sign == "+":
                stack.append(num)

            elif sign == "*":
                stack.append(stack.pop() * num)

            else:
                tmp = stack.pop()
                if tmp//num < 0 and tmp%num!=0:
                    stack.append(tmp//num+1)
                else:
                    stack.append(tmp//num)

            sign = string[i]
            num = 0

    return sum(stack)


def calc_test(num):

    to_return = 0

    for i in xrange(len(num)):

        to_return = to_return * 10 + ord(num[i]) - ord('0')

    return to_return

print calculator("3+2/2")

print type(calc_test("23"))
