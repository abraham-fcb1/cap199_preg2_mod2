
import pandas as pd
import matplotlib.pyplot as plt

# Cargar dataset
df = pd.read_csv("Cancer_Pulmon.csv")

fig, axes = plt.subplots(2, 2, figsize=(20, 12))
fig.suptitle('Cancer', fontsize=16, fontweight='bold')


# Histograma de la columna/variable : age
axes[0,0].hist(df['age'], bins=5, color='skyblue', edgecolor='black')
axes[0,0].set_title('Distribucion de la edad')
axes[0,0].set_xlabel('Edad')
axes[0,0].set_ylabel('Frecuencia')
axes[0,0].grid(alpha=0.3)


# Diagrama de tipo pie de la variable/columna : gender
df['gender'].value_counts().plot.pie(
    autopct='%1.1f%%',
    colors=['tab:blue', 'tab:orange'],
    ax=axes[0,1]
)
axes[0,1].set_title('Distribucion del genero')
axes[0,1].set_ylabel('')


# Distribucion de paises (Columna : country) en un diagrama de barras
df['country'].value_counts().plot.bar(
    color='lightcoral',
    ax=axes[1,0],
    width=0.9
)
axes[1,0].tick_params(axis='x', rotation=90)
axes[1,0].set_title('Pacientes por pais')
axes[1,0].set_ylabel('Numero de pacientes')
axes[1,0].grid(axis='y', alpha=0.3)


# Distribucion de la etapa del cancer (columna cancer_stage) en un diagrama de barras
df['cancer_stage'].value_counts().plot.bar(
    color='lightgreen',
    ax=axes[1,1],
    width=0.8
)
axes[1,1].set_title('Distribucion de la etapa del cancer')
axes[1,1].set_ylabel('Numero de observaciones')
axes[1,1].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()
