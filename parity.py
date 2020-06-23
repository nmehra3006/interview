def parity(number):
    bit = None
    n = 32
    while len(number) > 8:
        number  = number ^ (number >> n)

        n = n // 2

    return table[num & 0xff]