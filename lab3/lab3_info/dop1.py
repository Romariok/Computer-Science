import re

def readfile(s):
    tmp = open(s, encoding='utf8')
    tmp1 = ''
    for i in tmp.readlines():
        tmp1 += i
    tmp.close()
    return tmp1

def subtime(s):
    t1 = r'[0-1][0-9]:[0-5][0-9]:[0-5][0-9][\s\.,()]'
    tmp = re.sub(t1,"(TMD) ", s)
    t1 = r'2[0-3]:[0-5][0-9]:[0-5][0-9][\s\.,()]'
    tmp = re.sub(t1,"(TMD) ", tmp)
    t1 = r'[0-1][0-9]:[0-5][0:9][\s\.,()]'
    tmp = re.sub(t1,"(TMD) ", tmp)
    t1 = r'2[0-3]:[0-5][0:9][\s\.,()]'
    tmp = re.sub(t1,"(TMD) ", tmp)
    return tmp


print("Введите тип взаимодействия с программой\n1 - Встроенные тесты\n2 - Саммостоятельное введение текста")
k = int(input())
if k == 1:
    print(subtime(readfile("dop1_tests/dop1_test.txt")))
    print('')
    for i in range(1,6):
        print(subtime(readfile("dop1_tests/dop1_test"+str(i)+".txt")))
        print('')

else:
    print("Введите путь вашего теста относительно программы")
    path = str(input())
    print(subtime(readfile(path)))