import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from fuzzywuzzy import process
#necesario -> pip install pandas matplotlib seaborn geopandas fuzzywuzzy python-Levenshtein openpyxl xlrd

internet_access_data = pd.read_excel('./Dataset/API_IT.NET.USER.ZS_DS2_en_excel_v2_26497.xls', skiprows=3)

internet_access_data.columns = ['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'] + [str(year) for year in range(1960, 2024)]
internet_access_data_clean = internet_access_data[['Country Name', '2023']].dropna()
internet_access_data_clean.columns = ['Country', 'Access_2023']

shapefile_path = 'geopanda/ne_110m_admin_0_countries.shp'
world = gpd.read_file(shapefile_path)

def fuzzy_merge(df_1, df_2, key1, key2, threshold=90):
    s = df_2[key2].tolist()
    matches = df_1[key1].apply(lambda x: process.extractOne(x, s))
    df_1["Best Match"] = matches.apply(lambda x: x[0] if x[1] >= threshold else None)
    return df_1

internet_matched = fuzzy_merge(internet_access_data_clean.copy(), world, 'Country', 'ADMIN', threshold=85)

internet_matched = internet_matched.dropna(subset=['Best Match'])
merged = world.set_index('ADMIN').join(internet_matched.set_index('Best Match'))

fig, ax = plt.subplots(1, 1, figsize=(18, 10))
merged.plot(column='Access_2023', ax=ax, legend=True,
            legend_kwds={'label': "Acceso a Internet (% población, 2023)", 'orientation': "horizontal"},
            cmap='viridis', edgecolor='black', linewidth=0.4)

ax.set_title("Mapa mundial de acceso a Internet en 2023", fontsize=18, weight='bold')
ax.set_axis_off()

plt.show()
