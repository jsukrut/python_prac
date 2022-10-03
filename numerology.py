import string

alphabets = [ alpha for alpha in string.ascii_uppercase]
numerlogy_number_chart = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
    'F': 8, 'G': 3, 'H': 5, 'I': 1, 'J': 1,
    'K': 2, 'L': 3, 'M': 4, 'N': 5, 'O': 7,
    'P': 8, 'Q': 1, 'R': 2, 'S': 3, 'T': 4,
    'U': 6, 'V': 6, 'W': 6, 'X': 5, 'Y': 1,
    'Z': 7
}
def final_sum(no):
    return no if no < 10 else int(final_sum(no % 10 + final_sum(no / 10)))

#calcuate destiny number

name = input("Enter your First Name")
name =name.upper()

density_sum = 0
for char in name:
    if char in numerlogy_number_chart:
        number= int(numerlogy_number_chart.get(char))
        density_sum = density_sum+ number
print("Density Sum",density_sum)
print("Density Number",final_sum(density_sum))

soul_urge_sum = 0
for char in name:
    if char in ['A','E','I','O','U']:
        number = int(numerlogy_number_chart.get(char))
        soul_urge_sum = soul_urge_sum + number

print("Soul Urge Sum",soul_urge_sum)
print("Soul Urge Number",final_sum(soul_urge_sum))



personality_sum = 0
for char in name:
    if char not in ['A','E','I','O','U']:
        number = int(numerlogy_number_chart.get(char))
        personality_sum = personality_sum + number

print("personality Sum",personality_sum)
print("personality Number",final_sum(personality_sum))

