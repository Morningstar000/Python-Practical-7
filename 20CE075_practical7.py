# 20CE075 PARTH PARMAR
# Practical 7
# Aim : Lapindrome is defined as a string which when split in the middle, gives two halves having the same characters and same frequency of each character.
# If there are odd number of characters in the string, we ignore the middle character and check for lapindrome. For example gaga is a lapindrome,
# since the two halves ga and ga have the same characters with same frequency. Also, abccab, rotor and xyzxy are a few examples of lapindromes.
# Note that abbaab is NOT a lapindrome. The two halves contain the same characters but their frequencies do not match.
# Your task is simple. Given a string, you need to tell if it is a lapindrome.
# https://github.com/Morningstar000/Python-Practical-7

t = int(input())
dict0 = {}
list0 = []

for i in range(t):
    str0 = input()
    list0.append(str0)
    if str0 not in dict0:
        dict0[str0] = 1
    else:
        dict0[str0] += 1

print(len(dict0))
print(' '.join([str(dict0[word]) for word in dict0]))
