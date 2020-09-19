

def RussianMul(m, n):
    remain = 0
    while m != 1:
        if m % 2 != 0:
            m = (m - 1) >> 1
            remain += n
            n = n << 1
        else:
            m = m >> 1
            n = n << 1
    return n + remain


if __name__ == '__main__':
    print(RussianMul(13, 9))
