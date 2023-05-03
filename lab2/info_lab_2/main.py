def xor(x1, x2, x3, x4):
    ans = 0
    if x1 != x2:
        ans = 1
    else:
        ans = 0
    if ans != x3:
        ans = 1
    else:
        ans = 0
    if ans != x4:
        ans = 1
    else:
        ans = 0
    return ans

n = input()
ans = ''
k = ''
er_bit = 0
s1 = xor(int(n[0]), int(n[2]), int(n[4]), int(n[6]))
s2 = xor(int(n[1]), int(n[2]), int(n[5]), int(n[6]))
s3 = xor(int(n[3]), int(n[4]), int(n[5]), int(n[6]))
if s1 == s2 == s3 == 0:
    print('Правильное сообщение: ', n[2]+n[4:])
else:
    k = str(s1)+str(s2)+str(s3)
    k = k[2]+k[1]+k[0]
    er_bit = int(k, 2)
    if n[er_bit-1] == '0':
        ans = n[:er_bit-1]+'1'+n[er_bit:]
    else:
        ans = n[:er_bit-1]+'0'+n[er_bit:]
    print('Правильное сообщение: ', ans[2]+ans[4:])
    print('Номер ошибочного бита = ', er_bit)
