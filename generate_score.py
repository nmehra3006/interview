def generate_score(string):

    stack = [0]
    for s in string:
        if s == "(":
            stack.append(0)
        else:
            v = stack.pop()
            stack[-1] += max(2*v, 1)
    return stack.pop()


print generate_score("(())()")


