str1 = input("Enter text: ")
file_name = input("Enter filename: ")

with open(file_name, 'rt') as in_f:
   with open('out.txt', 'wt') as out_f:
      for line in in_f:
         lst = line.split('|')
         out_f.write('|'.join(lst[:3] + ['що небудь'] + lst[3:]))
