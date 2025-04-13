import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib.cm as cm

df = pd.read_csv("Global_Tech_Gadget_Consumption.csv")
df_pivot = df.pivot(index="Year", columns="Country", values="5G Penetration Rate (%)")

countries = df_pivot.columns.tolist()
years = df_pivot.index.values
offset = 55
n_colors = len(countries)
colors = cm.viridis(np.linspace(0.1, 0.9, n_colors))

plt.figure(figsize=(12, 10))

for i, (country, color) in enumerate(zip(countries, colors)):
    data = df_pivot[country].fillna(0).values
    y_offset = (len(countries) - i - 1) * offset

    xnew = np.linspace(years.min(), years.max(), 300)
    spline = make_interp_spline(years, data, k=2)
    smooth = spline(xnew)

    plt.fill_between(xnew, y_offset, smooth + y_offset, color=color, alpha=0.9)
    plt.plot(xnew, smooth + y_offset, color="black", linewidth=0.5, alpha=0.6)
    plt.text(years.min() - 0.5, y_offset + offset / 3, country, ha='right', va='center', fontsize=9)

plt.title("Penetración 5G por País y Año", fontsize=14)
plt.xlabel("Año")
plt.yticks([])
plt.grid(axis='x', linestyle='--', alpha=0.3)
plt.tight_layout()
plt.show()
