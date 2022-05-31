#Посимвольное шифрование---------------------------------------------------------
def SymbEnc(text, key):
    ost_len = len(text) % len(key)
    text += ((len(key) - ost_len) % len(key)) * '\0'
    tempt = ""
    ost_text = ""
    if len(key)<len(text):#если ключ меньше чем текст, вызываю рекурсию для всего текста без первой части
        ost_text = text[len(text)-len(key):]
        ost_text = SymbEnc(ost_text,key)
    for i in range(len(text)):
        counter = 0
        for j in key:
            if int(j) == i and text[counter] != "\0":
                if tempt != "":
                    while tempt[-1] == "\0":
                        tempt = tempt[:-1]
                tempt+= text[counter]
                break
            counter+=1
    tempt+=ost_text #пихаем в конец остаток
    return tempt
#Шифрование группами-----------------------------------------------------------------------
def GroupEnc(text,key,groupsym):
    if groupsym == "1":
        res = SymbEnc(text,key)
    text += (len(key) * int(groupsym) - len(text)) * '\0'
    text1 = []
    for i in range(0, len(text), int(groupsym)): 
        text1.append(text[i:i + int(groupsym)])
    res = SymbEnc(text1,key)
    return res
#Шифрование пословно------------------------------------------------------------------------
def WordEnc(text,key):
    text = text.split(" ")
    ost_len = len(text) % len(key)
    text += ((len(key) - ost_len) % len(key)) * '\0'
    tempt = ""
    probel = " "
    ost_text = ""
    if len(key)<len(text):
        ost_text = text[len(text)-len(key):]
        ost_text = SymbEnc(ost_text,key)
    for i in range(len(text)):
        c = 0
        for j in key:
            if int(j) == i and text[c] != "\0":
                if tempt != "":
                    while tempt[-1] == "\0":
                        tempt = tempt[:-1]
                tempt+= text[c]+ probel
                break
            c+=1
    tempt+=ost_text
    return tempt
#Расшифровка посимвольная--------------------------------------------------------------------
def SymbUnEnc(text, key):
    ost_len = len(text) % len(key)
    text += ((len(key) - ost_len) % len(key)) * '\0'
    tempt = ""
    ost_text = ""
    if len(key)<len(text):
        ost_text = text[len(text)-len(key):]
        ost_text = SymbEnc(ost_text,key)
    for j in key:
            if tempt != "":
                while tempt[-1] == "\0":
                    tempt = tempt[:-1]
            tempt+= text[int(j)]
    tempt+=ost_text 
    return tempt
#Расшифровка группами---------------------------------------------------------------------
def GroupUnEnc(text,key,groupsym):
    if groupsym == "1":
        res = SymbUnEnc(text,key)
    text += (len(key) * int(groupsym) - len(text)) * '\0'
    text1 = []
    for i in range(0, len(text), int(groupsym)): 
        text1.append(text[i:i + int(groupsym)])
    res = SymbUnEnc(text1,key)
    return res
#Расшифровка пословно-----------------------------------------------------------------------
def WordUnEnc(text, key):
    text = text.split(" ")
    ost_len = len(text) % len(key)
    text += ((len(key) - ost_len) % len(key)) * '\0'
    tempt = ""
    probel = " "
    ost_text = ""
    if len(key)<len(text):#если ключ меньше чем текст, вызываю рекурсию для всего текста без первой части
        ost_text = text[len(text)-len(key):]
        ost_text = SymbEnc(ost_text,key)
    for j in key:
            if tempt != "":
                while tempt[-1] == "\0":
                    tempt = tempt[:-1]
            tempt+= text[int(j)]+probel
    tempt+=ost_text #пихаем в конец остаток
    return tempt
#проверка корректности ключа-----------------------------------------------------------------
def valkey(key):
    for k in key:
        if not k.isdigit() or len(k) > 1:
            return False
    p2 = []
    p1 = sorted(key)
    for i in range(len(key)):
        p2.append(str(i))
    return p1 == p2
#Интерфейс--------------------------------------------------------------------------------------
print("Добро пожаловать в меню, выберите действие:")
print("1. Шифрование     2.Расшифрование",end = " ")
mode = input()
while mode not in ("1","2"):
    mode = input("Убедитесь в корректности введённых данных.\n1. Шифрование     2.Расшифрование.")
print("Виды шифрования и расшифрования: \n1.Посимвольно 2.Группами символов 3.Пословно",end = " ")
typ3 = input()
while typ3 not in ("123"):
    typ3 = input("Убедитесь в корректности введённых данных.\n")
if typ3 == "2":
    groupsym = input("Введите длинну групп символов: ")
    while not groupsym.isdigit():
        groupsym = input('Пожалуйста, введите корректное значение: ')
key = input('Введите ключ используя пробел, например "1 0 3 2":\n').split(' ')
while not valkey(key):
    key = input('Пожалуйста, введите корректное значение используя пробел, например "1 0 3 2":\n').split(' ')
#шифрование-------------------------------------------------------------------
text = input("Введите текст:\n")
if typ3 == "1":
    if mode == "1":
        result = SymbEnc(text,key)              #шифровка посимвольно
    else:
        result = SymbUnEnc(text,key)            #расшифровка посимвольно
if typ3 == "2":
    if mode == "1":
        result = GroupEnc(text,key,groupsym)    #шифровка группами
    else:
        result = GroupUnEnc(text,key,groupsym)  #расшифровка группами
if typ3 == "3":
    if mode == "1":
        result = WordEnc(text,key)              #шифровка пословно
    else:
        result = WordUnEnc(text,key)            #расшифровка пословно
#вывод
print("Результат сложных вычислений: ",result)

    

