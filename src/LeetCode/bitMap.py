N = 10000000
a = [0 for i in range(int(N/32 + 1))]
print(a)

def addValue(n):
    row = n >> 5
    a[row] |= 1 << (n & 0x1F)


def exits(n):
    row = n >> 5
    return (a[row] & (1 << (n & 0x1F))) is 1


num = [1, 5, 30, 32, 64, 56, 159, 120, 21, 17, 35, 45]
for i in range(len(num)):
    addValue(num[i])
temp = 120
print("num中是否存在120：", exits(temp))

