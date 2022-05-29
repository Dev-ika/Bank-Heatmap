import pandas as pd 
import geopandas as gpd
import matplotlib.pyplot as plt 

df = pd.read_csv('./data/IFSC.csv',low_memory=False)
print(df.head(5))

shp_gdf = gpd.read_file('./data/india_st.shp')
print(shp_gdf.head(5)) 

merged = shp_gdf.set_index('STATE').join(df.set_index('STATE'))
print(merged.head(5))


# fig, ax = plt.subplots(1, figsize=(12, 12))
# ax.axis('off')
# ax.set_title('Banks as per state',
#              fontdict={'fontsize': '15', 'fontweight' : '3'})
# fig = merged.plot(column='bank', cmap='RdYlGn', linewidth=0.5, ax=ax, edgecolor='0.2',legend=True)