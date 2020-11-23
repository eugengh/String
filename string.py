import re
s=str(input("Sirul: "))
print(len(re.findall(r'[A-Z]', s)))
print(len(re.findall(r'[0-9]', s)))
print(len(re.findall(r'[@_!#$%^&*()<>?/\|}{~:]', s)))