def isValid(string):

    i = 0
    bal = 0
    while i < len(string):
        if string[i] == "(":
            bal += 1
        else:
            bal -= 1
        if bal < 0:
            return False
        i +=1

    return bal == 0

def generate_p(string):
    max_len = 0
    start = 0
    for i in range(len(string)):
        for j in range(i, len(string)+1, 2):
            if isValid(string[i:j]):
                if (j-i) > max_len:
                    max_len = j-i
                    start = i

    return string[start:start+max_len]

print generate_p("))))((((")