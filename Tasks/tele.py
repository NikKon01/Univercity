def get_num():
    num = input("Введите номер телефона: ")
    num = num.replace(" ", "").replace("-", "")

    if (num[0] == "8") and (len(num) == 11):
        num = num.replace("8", "+7", 1)
    if (num[0] == "7") and (len(num) == 11):
        num = "+" + num
    if (num[0] == "9") and (len(num) == 10):
        num = "+7" + num
    if (len(num) == 12) and (num[1:].isdigit()):
        return(num)
    else:
        print("Неправильно набран номер!")
        return get_num()

def get_name():
    name = input("Введите имя: ")
    name = name.title()
    return name

def get_contact(dict, names, num):
    dict[names] = num
    print("Контакт добавлен")
    return dict

def remove_contact (dict, names)
    if not (names in dict):
        print("Нет такого номера!")
        return False
    del dict[names]
    return dict

def show_dict(dict):
    print("Список контактов")
    for i in dict:
        print(i, dict[i])

def change_num(dict, names):
    if not (names in dict):
        print("Нет такого номера!")
        return False
    dict[names] = get_num()
    print("Контакт изменён")
    return(dict)

i = 0
dict = {}

while True:






