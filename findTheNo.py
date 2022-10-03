# Write a code for finding any two (or three) numbers in the given array whose sum is equal to x.

# no_list = [ i for i in range(1,100)]
no = int(input("Enter the no"))
no_list = [ i for i in range(1,no)]

using_two_numbers =[]
using_three_numbers =[]
for i in no_list:
    for j in no_list:
        if i+j == no:
            using_two_numbers.append([i,j])
print("----using_two_numbers",using_two_numbers,len(using_two_numbers))

for i in no_list:
    for j in no_list:
        for k in no_list:
            if i+j+k == no:
                using_three_numbers.append([i,j,k])
print("----using_three_numbers",using_three_numbers,len(using_three_numbers))


