import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('affiliates.csv')

df['porcentagem'] = (df['payment']  / 100) * 10

# condições sobre porcentagem
conditionmenor100 = (df['payment'] < 100) #10%
condition200 = (df['payment'] <= 200) & (df['payment'] > 100) #15%
condition300 = (df['payment'] <= 300) & (df['payment'] > 200) #20%
condition400 = (df['payment'] <= 400) & (df['payment'] > 300) #25%
condition500 = (df['payment'] <= 500) & (df['payment'] > 400) #30%
conditionmaior500 = (df['payment'] > 500) #50%

#inserindo variaveis de porcentagem
until100 = 10
until200 = 15
until300 = 20
until400 = 25
until500 = 30
over500 = 50

# Aplicar a lógica apenas nas linhas que atendem à condição
df.loc[df['payment'] <= 200, 'porcentagem'] = 15

# convertendo porcentagem para valor final
porcent = df['payment'] * (1 + until200 / 100)
print(porcent)
df['pgt_final'] = porcent


print(df.head(5))

# Identificar clientes com margem maior que 15%
clientes_maior_15 = df[df['porcentagem'] > 15]

#exibir grafico
plt.hist(df['porcentagem'], bins=20, color='blue', alpha=0.7, label='Todos os Clientes')
plt.hist(clientes_maior_15['porcentagem'], bins=20, color='orange', alpha=0.7, label='Margem > 15%')
plt.xlabel('Margem (%)')
plt.ylabel('Número de Clientes')
plt.title('Distribuição da Margem de Lucro')
plt.legend()

plt.show()