'''У введеному реченні змінити регістр всіх букв. Наприклад:
рядок “I`m eaTinG BaNaNa.” має бути конвертований у “i`M EAtINg bAnAnA.”
'''

str1 = "I'm eaTinG BaNaNa."
str_reverse = ""
for s in str1:
    if s.islower():
        s = s.upper()
        str_reverse = str_reverse + s
    elif s.isupper():
        s = s.lower()
        str_reverse = str_reverse + s
print(str_reverse)    