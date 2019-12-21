


def longestCommonPrefix(strs) -> str:
    """

    :param strs:
    :return:
    """
    if len(strs) == 0:
        return ""
    str_1 = strs[0]
    res = ""

    for i in range(len(str_1)):
        flag = 0
        for j in range(len(strs)):
            try:
                if str_1[i] != strs[j][i]:
                    flag = 1
                    break
            except:
                flag = 1
                break
        if flag == 1:
            break
        else:
            res += str_1[i]
    return res


print(longestCommonPrefix(["aa","a"]))


print(list(zip(["flower","flow","flight"])))























