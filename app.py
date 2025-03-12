def split(num: str ):
    if len(num) <= 1:
        return int(num)
    res = sum(int(i) for i in list(num))
    return split(str(res))

print(split("38"))