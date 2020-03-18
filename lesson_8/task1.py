'''
Написати програму, яка вставлятиме певний рядок всередину тексту. 
Програма повинна просити в користувача ім’я файлу, рядок, 
який треба вставити, і позицію рядка.
'''
file_path = input("Enter file path: ")
file = open(file_path, "r+")
string = input("Enter string: ")
line_number = int(input("Enter line number: "))
lines_before = open(file_path, "r+").readlines()[:line_number]
lines_after = open(file_path, "r+").readlines()[line_number-1:]
new_file = "".join(lines_before) + string + "".join(lines_after)
file.write(new_file)
file.close()
