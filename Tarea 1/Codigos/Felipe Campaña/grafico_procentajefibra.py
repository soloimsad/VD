import pandas as pd
from pywaffle import Waffle
import matplotlib.pyplot as plt
#necesario -> pip install pandas matplotlib pywaffle


file_path = "./Dataset/API_IT.NET.BBND.P2_DS2_en_excel_v2_14959.xlsx"
df = pd.read_excel(file_path, sheet_name="Data", skiprows=3)

df_long = df.melt(
    id_vars=["Country Name", "Country Code", "Indicator Name", "Indicator Code"],
    var_name="Year",
    value_name="Broadband Subscriptions (%)"
)

df_long["Year"] = pd.to_numeric(df_long["Year"], errors="coerce")
df_long = df_long.dropna(subset=["Year", "Broadband Subscriptions (%)"])

df_2023 = df_long[(df_long['Year'] == 2023) & (df_long["Broadband Subscriptions (%)"] > 0)]

top_n = 10
top_countries = df_2023.nlargest(top_n, "Broadband Subscriptions (%)")
waffle_data = top_countries.set_index("Country Name")["Broadband Subscriptions (%)"].round()

# 
fig = plt.figure(
    FigureClass=Waffle,
    rows=10,
    values=waffle_data,
    title={'label': 'Contraste en suscripciones de fibra por país (2023)', 'loc': 'center'},
    labels=[f"{k} ({v}%)" for k, v in waffle_data.items()],
    legend={'loc': 'lower left', 'bbox_to_anchor': (0, -0.4), 'ncol': 2},
    figsize=(10, 6)
)

plt.show()
