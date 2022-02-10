import pandas as pd
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# reading and transform csv into dataframe (for the news coordinates)
utm_new = pd.read_csv("coordinates_new.csv")

# visualize df
print("Header do arquivo new_coordinates:\n" )
print(utm_new.head())

# reading and transform csv into dataframe (for the olds coordinates)
utm_old = pd.read_csv("coordinates_old.csv")

# visualize df
print("Header do arquivo old_coordinates:\n" )
print(utm_old.head())

print("Criando gráfico 3D...")
fig, ax = plt.subplots(figsize=(15,15),subplot_kw={"projection": "3d"})

# Data for a three-dimensional line
X = utm_new["SIRGAS - Easting"]
Y = utm_new["SIRGAS - Northing"]
Z = utm_new["SIRGAS - Altura"]
line = ax.plot(X, Y, Z, label = "New Coordinates")

X = utm_old["SIRGAS - Easting"]
Y = utm_old["SIRGAS - Northing"]
Z = utm_old["SIRGAS - Altura"]
line2 = ax.plot(X, Y, Z, label = "Old Coordinates")

ax.set(title="Coordinates comparison", 
        xlabel="Easting (m)", 
        ylabel="Northing (m)",
        zlabel="Height (m)");
ax.legend();
fig.savefig('desafio1.png', dpi=fig.dpi);
plt.show();