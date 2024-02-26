import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel('Py.xlsx')  

plt.figure(figsize=(10, 6))
plt.bar(df['Luna'], df['Venit'] - df['Investitie'], color='purple')


plt.xlabel('Luna')
plt.ylabel('Profit')
plt.title('Profitul investiției în funcție de lună')
plt.xticks(rotation=45)  


plt.tight_layout()
plt.show()
