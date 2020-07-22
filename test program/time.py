import time;  # Digunakan untuk meng-import modul time

ticks = time.time()
print ("Berjalan sejak 01/01/1970:", ticks)

from datetime import time
cth_waktu = time(20, 31, 7) # parameter: jam, menit,detik
print(cth_waktu)
cth_waktu = time(hour = 8, second = 56) # 
print(cth_waktu)
print('')
# Format tanggal dan waktu dengan strftime
from datetime import datetime
saat_ini = datetime.now()
jam = saat_ini.strftime('%H:%M:%S')
print('Jam:', jam)
tgl = saat_ini.strftime('%d/%m/%Y') # format dd/mm/YY
print('Tanggal:', tgl)
tgl_jam = saat_ini.strftime("%d/%m/%Y, %H:%M:%S") # format dd/mm/YY H:M:S 
print('tanggal dan jam: ', tgl_jam)
print(saat_ini)
print('')
from datetime import datetime as dtm
tgl_text = '27-07-2005'
print(tgl_text, type(tgl_text)) # tipe data str
tgl_date = dtm.strptime(tgl_text,'%d-%m-%Y') # konversi string ke date dengan format tertentu
print(tgl_date, type(tgl_date)) # tipe data datetime.datetime

# print('Detik dari',tgl_text,'=',setdetik)