#Operasi Logika atau Boolean (Tabel Kebenaran)
# not, or, and, xor (^)

#not
print('\n===NOT===\n')
a = False
c = not a
print('Data a=',a)
print('Data b=',c)

#or (jika salah satu true maka hasilnya true)
print('\n===OR===\n')
a = False
b = False
c = a or b
print(a,'or',b,'=',c)
a = False
b = True
c = a or b
print(a,'or',b,'=',c)
a = True
b = False
c = a or b
print(a,'or',b,'=',c)
a = True
b = True
c = a or b
print(a,'or',b,'=',c)

#and (jika dua buah nilai true, maka hasil true)
print('\n===AND===\n')
a = False
b = False
c = a and b
print(a,'and',b,'=',c)
a = False
b = True
c = a and b
print(a,'and',b,'=',c)
a = True
b = False
c = a and b
print(a,'and',b,'=',c)
a = True
b = True
c = a and b
print(a,'and',b,'=',c)

#xor ^ (hasil true jika hanya salah satu nilai true)
print('\n===XOR===\n')
a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
a = False
b = True
c = a ^ b
print(a,'XOR',b,'=',c)
a = True
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
a = True
b = True
c = a ^ b
print(a,'XOR',b,'=',c)
