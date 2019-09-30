

def plusOne(digits):
    if digits[0] == 0:
        return [1]
    newdigists = list(reversed(digits))
    temp = newdigists[0] + 1
    pre = temp // 10
    newdigists[0] = temp % 10
    i = 1
    while pre > 0 and i < len(newdigists):
        temp = newdigists[i] + pre
        pre = temp // 10
        newdigists[i] = temp % 10
        i += 1
    if pre != 0:
        newdigists.append(pre)
    return list(reversed(newdigists))


print(plusOne([4,3,2,2]))