import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import geopandas as gpd # Import geopandas again
from Modules.Utils.add_df import coffee_data

url_mapa = "https://raw.githubusercontent.com/edavgaun/topojson/080eb96a46307efd0c4a31f4c11ccabeee5e97dd/countries/us-states/NJ-34-new-jersey-counties.json"

df_coffee_tea = coffee_data()

def new_nj_map(url_mapa, df_coffee_tea):
  # === 1. Extract county names from the geojson data ===
  # Read the geojson file again to ensure we have the data
  nj_data = gpd.read_file(url_mapa)
  
  # Assuming the county names are in a column named 'NAME' within the geojson properties
  # If the column name is different, you'll need to inspect nj_data.columns to find it.
  # Let's assume the column is 'NAME' based on the previous attempt.
  if 'NAME' in nj_data.columns:
      county_names = nj_data['NAME']
  else:
      # Fallback: Try to find a column that likely contains names based on previous attempt
      col_name = [c for c in nj_data.columns if "NAME" in c]
      if col_name:
          county_names = nj_data[col_name[0]].map(lambda x: str(x).replace('NAME:"','').replace('"',''))
      else:
          county_names = ["Unknown"] * len(nj_data) # Assign placeholder if names are not found
  
  # Assign the names to the nj GeoDataFrame
  nj = nj.copy() # Create a copy to avoid SettingWithCopyWarning
  nj["NAME"] = county_names.values
  
  # === 2. Calculate centroids of each polygon ===
  nj["centroid"] = nj.geometry.centroid
  
  # === 3. Crear el mapa hexagonal ===
  fig, axs = plt.subplots(figsize=(12, 10), facecolor="white")
  
  hb = axs.hexbin(
      df_coffee_tea["longitude"],
      df_coffee_tea["latitude"],
      gridsize=10,          # tamaño de los hexágonos
      cmap="CMRmap_r",
      mincnt=1,             # solo mostrar hexágonos con datos
      alpha=0.9,
  
  )
  
  # Contorno del mapa
  nj.boundary.plot(ax=axs, edgecolor="black", linewidth=1.2)
  
  # Barra de color
  cb = fig.colorbar(hb, ax=axs)
  cb.set_label("Número de Coffee & Tea Shops")
  
  # === 4. Colocar etiquetas en los centroides ===
  for idx, row in nj.iterrows():
      # Ensure row["centroid"] is a valid point geometry
      if row["centroid"] is not None and row["centroid"].is_valid:
          axs.text(
              row["centroid"].x,
              row["centroid"].y,
              row["NAME"],
              fontsize=8,
              color="gray",
              ha="center",
              va="center",
              weight="bold",
              bbox=dict(facecolor="white", alpha=0.6, edgecolor="none", boxstyle="round,pad=0.2")
          )
  
  # Ajustes finales
  axs.axis("off")
  axs.set_title("Coffee & Tea Shops in NJ", fontsize=18, weight="bold")
  plt.tight_layout()
  st.pyplot(fig)
