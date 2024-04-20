str1 ="a,a,a,b,b,c,c,c"

output ="a:3,b:2,c:3"

chars = str1.split(",")

checked_chars =[]
final=[]
for char in chars:
    if char not in checked_chars:
        checked_chars.append(char)
        final.append(char+":"+str(chars.count(char)))


print(",".join(final))
