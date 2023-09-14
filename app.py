import pandas as pd
import requests
import openpyxl as xl
import matplotlib.pyplot as plt 
import numpy as np
df_commodity = pd.read_excel('Commodity_Terms_of_Trade_Commodity_.xlsx')
column_lists = [df_commodity[column].tolist() for column in df_commodity.columns]

indices_brasil= column_lists[0]
indices_brasil.remove("Brazil")
indices_china = column_lists[1]
indices_china.remove("China")
indices_japan = column_lists[2]
indices_japan.remove("Japan")
indices_eua = column_lists[3]
indices_eua.remove("EUA")
indices_venezuela = column_lists[4]
indices_venezuela.remove("Venezuela")

indices_paises= [indices_brasil,indices_china,indices_japan,indices_eua,indices_venezuela]

vetor = np.vectorize(np.int_)

y1 = vetor(indices_brasil)
y2 = vetor(indices_china)
y3 = vetor(indices_japan)
y4 = vetor(indices_eua)
y5 = vetor(indices_venezuela)

x = (np.arange(11))

width = 0.30
largura = 0.350

fig, ax = plt.subplots(figsize=(12,8))
ax.bar(x-largura/2,y1, width  , color = 'cyan')
ax.bar(x + largura/2,y2, width , color = 'yellow')
ax.bar(x-largura/2,y3, width , color = 'silver')
ax.bar(x+largura/2,y4, width , color = 'orange')
ax.bar(x-largura/2,y5, width , color = 'green')
plt.legend(["Brasil", "China", "Japão","EUA","Venezuela"]) 

plt.show()