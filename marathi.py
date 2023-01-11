def devnagriNum(n):
    devn = ''
    for i in list(str(n)):
        if i.isdigit():
            devn += (chr(2406+int(i) ) )
        else: devn += i
    return devn

# test:

k = u'\u0905'
print(k)
print(devnagriNum(1))
print(devnagriNum(345)) # ३४५
print(devnagriNum(34.76)) # ३४.७६