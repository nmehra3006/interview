def decode_string(string):
    decoded = ""
    num = 0
    stack = []
    for c in string:
        if c.isdigit():
            num = num * 10 + int(c)
        elif c == '[':
            stack.append(num)
            stack.append(decoded)
            num, decoded = 0, ''
        elif c == ']':
            preStr = stack.pop()
            preNum = stack.pop()
            decoded = preStr + preNum * decoded
        else:
            decoded += c
    return decoded




print decode_string("3[a2[c]]")