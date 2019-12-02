

def combinationSum2(candidates, target):
    dic = {}
    for i in range(1, target + 1):
        dic[i] = []
    for i in range(1, target + 1):
        for e in candidates:
            if e == i and [i] not in dic[i]:
                dic[i].append([i])
            elif i > e:
                for k in dic[i - e]:
                    x = k[:]
                    y = candidates[:]
                    for j in x:
                        if j == e:
                            y.remove(e)
                    if e in x and e not in y:
                        continue
                    x.append(e)
                    x.sort()
                    if x not in dic[i]:
                        dic[i].append(x)
    return dic[target]


if __name__ == '__main__':
    print(combinationSum2([10,1,2,7,6,1,5], 8))

