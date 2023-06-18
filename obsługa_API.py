import requests, csv

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
print(data)
print(type(data))
a= data[0]
print(a['rates'])

with open('plik.csv', 'w', encoding='utf-8') as csvfile:
  csvwriter = csv.writer(csvfile)
  fieldnames = ['currency', 'code', 'bid', 'ask']
  csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames,delimiter=';')
  csvwriter.writeheader()
  for i in a['rates']:
    csvwriter.writerow(i)