import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Caricamento del DataFrame
df = pd.read_csv("Global_Education.csv", encoding="latin1")

# Calcolo della matrice di correlazione
df_numerical = df.select_dtypes(include=['number'])
correlation_matrix = df_numerical.corr()

# Creazione della heatmap
sns.heatmap(correlation_matrix)

# Visualizzazione del grafico
plt.savefig("test_heatmap.png")
plt.show() # may not show on Ubuntu

