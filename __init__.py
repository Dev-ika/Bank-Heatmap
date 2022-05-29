import pandas as pd 
import geopandas as gpd
import matplotlib.pyplot as plt 

df = pd.read_csv('./data/IFSC.csv',low_memory=False)
print(df.head(5))
df2 = pd.DataFrame(df.value_counts('STATE').rename_axis('STATE').reset_index(name='COUNTS'))
print (df2)

shp_gdf = gpd.read_file('./data/india_st.shp')
print(shp_gdf.head(5)) 

merged = shp_gdf.set_index('STATE').join(df2.set_index('STATE'))
print(merged.head(5))


# df['counts'] = df['STATE'].map(df['STATE'].value_counts())
# df_new = df[['STATE', 'counts']]
# df2.columns = ['STATE', 'BANK_COUNT']
print(df2.head(5))

fig, ax = plt.subplots(1, figsize=(12, 12))
ax.axis('off')
ax.set_title('Banks as per state',
             fontdict={'fontsize': '15', 'fontweight' : '3'})
fig = merged.plot(column='COUNTS', cmap='RdYlGn', linewidth=0.5, ax=ax, edgecolor='0.2',legend=True)
plt.show()