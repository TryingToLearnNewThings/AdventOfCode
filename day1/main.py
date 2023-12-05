import re


with open("aufgabe.txt", 'r') as str1:
    str1 = str1.readlines()


# string replace

original_string = [string for string in str1]
replacements = {'one': 'o1e', 'two': 't2o', 'three': 'th3ee', 'four': 'f4ur', 'five': 'fi5ve', 'six': 's6x', 'seven': 'se7en', 'eight': 'ei8ght', 'nine': 'ni9ne', 'zero': 'ze0ro'  }

for old, new in replacements.items():
    original_string = [re.sub(old, new, string) for string in original_string]

# ende string replace



total = 0
for line in original_string:
    digits = ''.join(filter(str.isdigit, line))
    if digits:
        filtered_line = (int(digits[0] + digits[-1]))
        total += filtered_line
        
        
print("Total is: ", total)
