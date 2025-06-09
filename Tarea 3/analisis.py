import pandas as pd
import matplotlib.pyplot as plt

# Carga tu archivo
df = pd.read_excel("Tarea 3/test.xlsx")

# Filtra por sabotaje y actores estatales
geo_conflict_df = df[(df['motive'] == 'Sabotage') & (df['actor_type'] == 'Nation-State')]

# Cuenta por país
conflict_counts = geo_conflict_df['country'].value_counts().sort_values(ascending=False)

# Crea el gráfico
plt.figure(figsize=(10, 6))
conflict_counts.plot(kind='barh', color='darkred')
plt.xlabel('Número de ataques saboteadores (Nation-State)')
plt.title('Ataques cibernéticos tipo Sabotage por actores estatales')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.grid(axis='x', linestyle='--', alpha=0.6)

# Guarda la imagen
plt.savefig("sabotage_state.png")
plt.show()
