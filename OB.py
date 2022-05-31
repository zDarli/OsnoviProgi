def SymEnc(text, key):
    ost_len = len(text) % len(key)
    text += ((len(key) - ost_len) % len(key)) * '\0'
    tempt = ""
    ost_text = ""
    if len(key)<len(text):#если ключ будет меньше чем текст, что не влезло просто пихается в конец
        ost_text = text[len(text)-len(key):]
    for i in range(len(text)):
        c = 0
        for j in key:
            if int(j) == i:
                tempt+=text[c]
            c+=1
    tempt+=ost_text #пихаем в конец остаток
    return tempt


#Интерфейс
print("Выберите действие:")
print("1. Шифрование  2.Расшифрование")
mode = input()
while mode not in ("1","2"):
    mode = input("Убедитесь в корректности введённых данных.\n")
print("Виды (рас)шифрования: \n1.Посимвольно 2.Группами символов 3.Словами")
typ3 = input()
while typ3 not in ("123"):
    typ3 = input("Убедитесь в корректности введённых данных.\n")
key = input('Введите ключ (через пробел, например "1 0 3 2"):\n').split(' ')
#шифрование
text = input("Введите текст:\n")
if typ3 == "1":
        result = SymEnc(text,key)  
print(result)

    

