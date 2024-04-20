def check_anagram(str1,str2):
    try:
        if str1 and str2:
            str1 = list(str1.replace(" ",'').lower())
            str2 = list(str2.replace(" ",'').lower())
            if str1.sort() == str2.sort():
                return "Anagram"
            else:
                return "Not Anagram"
    except Exception as e:
        print(e)
        raise e


str1 ="client eastwood"
str2 ="olsd west action"
print(check_anagram(str1,str2))