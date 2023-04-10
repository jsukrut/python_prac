
def is_palindrom(srtng):
    length = len(strng)
    for chr in range(0,int(length/2)):
        if strng[chr] != strng[length-chr -1]:
            return 0
        else:
            return 1

def reverse_str(strng):
    rev_strng =  [ strng[chr] for chr in range(len(strng)-1,-1,-1) ]
    return "".join(rev_strng)

strng = "mohini"
print(is_palindrom(strng))
print(reverse_str(strng))