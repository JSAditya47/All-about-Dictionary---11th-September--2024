
test_dict = {
    'Codingal': 3,
    'is': 2,
    'Best': 2,
    'for': 2,
    'Coding': 1
}

print("The Original Dictionary: " + str(test_dict))

k = int(input("Enter the value to check the frequency of: "))


res = 0

for key in test_dict:
    if test_dict[key] == k:
        res += 1

print("Frequency of " + str(k) + " is: " + str(res))

