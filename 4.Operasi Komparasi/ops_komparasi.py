#Operasi Komparasi

#Setiap hasil dari komparasi adalah Boolean

# < > <= >= == != is is not
# = (assignment), == (sama dengan), != (tidak sama dengan)
# is / is notsebagai komparasi object identity
x = 5 # = assignment membuat object, x = variable (tersimpan dalam memmory), 5 = literal
y = 5
print('Nilai X =',x,'- ID =',hex(id(x)))
print('Nilai Y =',y,'- ID =',hex(id(y)))
hasil = x is y
print('x is y =',hasil)