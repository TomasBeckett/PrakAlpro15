import re
import random
import string

emails = """
anton@mail.com dimiliki oleh antonius
budi@gmail.co.id dimiliki oleh budi anwari
slamet@getnada.com dimiliki oleh slamet slumut
matahari@tokopedia.com dimiliki oleh toko matahari
"""

email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

email_list = re.findall(email_pattern, emails)

for email in email_list:
    username = email.split('@')[0]
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    print(f"{email} username: {username} , password: {password}")
