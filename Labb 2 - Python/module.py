import json

dictionary = [] 

def ReadCsv(filename): 
    global dictionary
    container = []
    try:
        with open(filename, encoding='utf-8') as f_obj:
            for line in f_obj:
                container.append(line)
        for line in container:
            info = line.rstrip('\n').split(';')
            dictionary.append({'Name:': info[0], 'Ename:': info[1], 'Username:': info[2], 'Email:': info[3]})
    except FileNotFoundError as error:
        print(error)

def ToJson(filename):
    global dictionary
    try:
        with open(filename, "w", encoding="utf-8") as jf_dump:
            json.dump(dictionary, jf_dump, ensure_ascii=False, indent=4)
    except FileNotFoundError as error:
        print(error)

def ReadJson(filename):
    global dictionary
    with open(filename, "r", encoding="utf-8") as rj_obj:
        dictionary = json.load(rj_obj)
        for i in dictionary:
            print(i)

def AddPerson():
    global dictionary
    try:
        name = input('Enter firstname: ')
        ename = input('Enter Lastname: ')
        username = input('Enter Username:')
        mail = input('Enter Email: ')
        dictionary.append({
            'Name:': name,
            'Ename:': ename,
            'Username:': username,
            'Email:': mail
            })
    except ValueError as error:
        print(error)
        
"""def RemovePerson():
    try:
        remove = input('Enter username of the user you want to delete: ')
        for i in dictionary:
            if remove == dictionary[i]['Username:']:
                del dictionary[i]
    except ValueError as error:
        print(error)"""
 
def RemovePerson():
    global dictionary
    try:
        count = 0
        rem = input('Enter username to delete: ')
        for p in dictionary:
            if rem == p['Username:']:
                dictionary.pop(count)
            count += 1
    except ValueError as error:
        print(error)

