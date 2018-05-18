def mii():
    na = input()
    if len(na) >= 5 and any(x.isupper() for x in na):
        return True
    return False

print(mii())
