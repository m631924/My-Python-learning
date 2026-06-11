def mysplit(strng):
    result = []
    word = ""
    for i in range(len(strng)):
        w = strng[i]
        if w != " ":
            word = word + w
            if i == len(strng) - 1:
                result.append(word)
        elif w == " ":
            result.append(word)
            if result[-1] == "":
                result.pop(-1)
            word = ""
    return result

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
