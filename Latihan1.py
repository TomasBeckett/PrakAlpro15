import re
from datetime import datetime

teks = """
Pada tanggal 1945-08-17 Indonesia merdeka. Indonesia memiliki beberapa pahlawan nasional, seperti Pangeran Diponegoro (TL: 1785-11-11), Pattimura (TL: 1783-06-08) dan Ki Hajar Dewantara (1889-05-02).
"""

pola = r'\d{4}-\d{2}-\d{2}'

tanggal_list = re.findall(pola, teks)

tanggal_sekarang = datetime.now()

for tanggal_str in tanggal_list:
    tanggal_obj = datetime.strptime(tanggal_str, "%Y-%m-%d")
    
    delta_hari = (tanggal_sekarang - tanggal_obj).days
    
    formatted_tanggal = tanggal_obj.strftime("%Y-%m-%d %H:%M:%S")
    result = f"{formatted_tanggal} selisih {delta_hari} hari"
    print(result)
