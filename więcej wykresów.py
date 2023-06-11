
import pandas as pd
import matplotlib.pyplot as plt


prices = [
    (1, 2.12),
    (2, 2.56),
    (3, 3.10),
    (4, 3.16),
    (5, 3.58),
    (6, 5.12),
    (7, 5.16),
    (8, 5.20),
    (9, 4.12),
    (10, 4.10),
    (11, 3.65),
    (12, 4.25)
]


df = pd.DataFrame(prices, columns=['Miesiąc', 'CenaPLN'])

df.set_index('Miesiąc', inplace=True)

df['CenaUSD'] = df['CenaPLN'] / 4

df.plot(y='CenaUSD', color='red', linestyle='--')

plt.title('Ceny produktu w USD')
plt.xlabel('Miesiąc')
plt.ylabel('Cena w USD')


plt.show()







