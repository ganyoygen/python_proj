import time 
detik = time.time()
print("test")
a = 10
print(a) #test comment
print (detik, "detik")
""" multiline  
comment """

# compile python:
# phtyon -m py_compile <file.py>

# variable adalah tempat menyimpan data
#tipe data: kumpulan karakter (string)
print("")
print("variabel dan tipe data")
data_string = "1"
print("Data: ",data_string, "Type: ",type(data_string))

#tipe data: satuan (integer)
data_integer = 1
print("Data: ",data_integer, "Type: ",type(data_integer))

#tipe data: angka dengan koma (float)
data_float = 1.7
print("Data: ",data_float, "Type: ",type(data_float))

#tipe data: biner true/false (boolean)
data_bool = False
print("Data: ",data_bool, "Type: ",type(data_bool))

#tipe data khusus: bilangan kompleks
data_complex = complex(2,3)
print("Data: ",data_complex, "Type: ",type(data_complex))

#tipe data khusus: data dari bahasa C
from ctypes import c_char, c_double, c_int
data_c_char = c_int(20)
data_c_double = c_double(1.4)
print("Data: ",data_c_char, "Type: ",type(data_c_char))
print("Data: ",data_c_double, "Type: ",type(data_c_double))

#casting (merubah satu tipe ke tipe lain)
print("")
print("Casting")

print("====INTEGER====")
data_int = 8
print("Data:",data_int, "Type: ",type(data_int))

data_float  = float(data_int)
data_str    = str(data_int)
data_bool   = bool(data_int) #akan false jika nilai int = 0
print("Data:",data_float, "- Type:",type(data_float))
print("Data:",data_str, "- Type:",type(data_str))
print("Data:",data_bool, "- Type:",type(data_bool))

print("====STRING====")
data_str = "0"
print("Data:",data_str, "- Type: ",type(data_str))

data_float  = float(data_str) #string harus angka
data_int    = str(data_str) #string harus angka
data_bool   = bool(data_str) #akan false jika string kosong
print("Data:",data_float, "- Type:",type(data_float))
print("Data:",data_int, "- Type:",type(data_int))
print("Data:",data_bool, "- Type:",type(data_bool))

