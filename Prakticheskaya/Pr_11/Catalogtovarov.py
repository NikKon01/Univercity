import re
import ssl
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context
url = urllib.request.urlopen("https://quke.ru/shop/smartfony/apple?page-size=72").read().decode()

pricep = r'(?:<span class="b-card2-v2__price-val">)([^<]+)'
price = re.findall(pricep, url)
print(price)

phonep = r'(?:<a class="b-card2-v2__name" href=")(?:[^\"]+)(?:" title=")([^\"]+)'
phone = re.findall(phonep, url)
print(phone)

phpr = dict(map(lambda x, y: (x, int(y.replace(" ", ""))), phone, price))
kol = 72

min_price = min(phpr.values())
max_price = max(phpr.values())
sr_price = round(sum(phpr.values()) / kol)

print(min_price)
print(max_price)
print(sr_price)

f = open("catalog.txt", 'w')
for k, v in phpr.items():
    f.write(f'{k}: {v}\n')

f.write(f'\nmin: {str(min_price)} \n')
f.write(f'max: {str(max_price)} \n')
f.write(f'sr: {str(sr_price)} \n')