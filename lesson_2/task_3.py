'''На вхід отримати такі значення: name, mobile_phone, email. 
На екран вивести наступні речення: “Привіт, мене звати <name>. 
Мій мобільний - <mobile_phone>, електронна адреса - <email>”.'''

name = input("Name? ")
mobile_phone = input("Phone number? ")
email = input("Email? ")
print(f'Привіт, мене звати {name}.\nМій мобільний - {mobile_phone},\nЕлектронна адреса - {email}') #за допомогою f-string виводимо введену інформацію на екран