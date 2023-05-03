import re

def readfile(s):
    tmp = open(s, encoding='utf8')
    tmp1 = ''
    for i in tmp.readlines():
        tmp1 += i
    tmp.close()
    return tmp1

print("Введите тип взаимодействия с программой\n1 - Встроенные тесты\n2 - Саммостоятельное введений смайлика и текста")
k = int(input())
if k == 1:
    smile = r'=-\|'
    for i in range(1, 6):
        print("Количество вхождений смайлика в тексте "+str(i)+" = ", len(re.findall(smile, readfile("Smile_tests/Smile_test"+str(i)+".txt"))))


else:
    print("Введите ваш смайлик")
    smile = r''.join(str(input()))
    smile = re.escape(smile)
    print("Введите путь вашего теста относительно программы")
    path = str(input())
    t1 = re.findall(smile, readfile(path))
    print("Количество вхождений смайлика в тексте = ", len(t1))
