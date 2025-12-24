
import pandas as pd
import matplotlib.pyplot as plt

# Cargar dataset (item b)
df = pd.read_csv("Cancer_Pulmon.csv")

variables = ['age', 'bmi', 'cholesterol_level']

plt.figure(figsize=(12, 6))
plt.boxplot(
    [df[var] for var in variables],
    labels=variables,
    patch_artist=True
)

plt.title('Boxplots de variables clínicas')
plt.ylabel('Valores')
plt.grid(axis='y', alpha=0.3)

plt.show()
