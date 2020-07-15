#Kumpulan karakter

#bisa menggunakan "  '
'''
    1. menggunakan single quote '...'
    2. menggunakan double quote "..."
'''
string = "ini string"
print(string)
print("ini hari jum'at")

#membuat tanda ' menjadi string menggunakan \
print('ini hari jum\'at')

#backslash
print('C:\\user\\desktop') # hasil C:\user\desktop

#tab
print('text\ttab\t\t\ttext')

#backspace
print('text\btab text')

#newline (enter)
print('baris pertama \nbaris kedua') # LF = line Feed -> Linux
print('baris pertama \rbaris kedua') # CR = Carriage Return -> comodore, acorn
print('baris pertama \r\nbaris kedua') #CRLF -> Windows

#string literal atau raw string
print(r'C\user\desktop') # hasil C:\user\

#multiline literal 
print("""
ID: 0123123
Name: User
""")

#multiline literal dan raw string 
print(r"""
ID: 0123123
Name: User
Web: https://www.youtube.com/watch?v=fhAEh1Z9YuY
""")
 
 
 