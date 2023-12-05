import re


with open("aufgabe.txt", 'r') as str1:
    str1 = str1.readlines()

# print(re.sub("\D", "", str1))


filtered_lines = [re.sub("\D", "", line) for line in str1]
for filtered_line in filtered_lines:
    print(filtered_line)
