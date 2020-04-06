'''
Створити базовий клас File.Створити два інші класи (JsonFile, TxtFile), які наслідуватимуться від нього. 
Для даних класів реалізувати методи open_file, write_to_file. для JsonFile інформація у файл повинна 
записуватися у форматі json. Які атрибути повинні бути у класів: filename. Реалізувати також метод get_file_extension, 
який повертатиме формат файлу.
'''

class File:
    def __init__(self, filename, path):
        self.filename = filename
        self.path = path

    def open_file(self):
        pass

    def write_to_file(self):
        pass
    
    def get_file_extension(self):
        with open(f'{self.path}' + {self.filename}, 'r') as f:
            text = f.read()
        return text
        

class JsonFile(File):
    def __init__(self):
        
    import json

    trunk_template = [
        'switchport trunk encapsulation dot1q', 'switchport mode trunk',
        'switchport trunk native vlan 999', 'switchport trunk allowed vlan'
    ]

    access_template = [
        'switchport mode access', 'switchport access vlan',
        'switchport nonegotiate', 'spanning-tree portfast',
        'spanning-tree bpduguard enable'
    ]

    to_json = {'trunk': trunk_template, 'access': access_template}

    with open('sw_templates.json', 'w') as f:
        f.write(json.dumps(to_json))

    with open('sw_templates.json') as f:
        print(f.read())

class TxtFile(File):
    pass

txt = File.