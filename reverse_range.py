def reverse_range(string, start, finish):
    while start<finish:
        string[start], string[finish] = string[finish], string[start]
        string, finish = string+1, finish-1

print reverse_range("hello", 0, 4)