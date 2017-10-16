import folium
import pandas as pd
from folium.plugins import MarkerCluster
import os

#Center coordinates
SF_COORDINATES = (40.4168, -3.7038)

# for speed purposes
MAX_RECORDS = 10

os.chdir('/Volumes/MacintoshHD/_data/gasolineras')
files = os.listdir()
files.sort()
files[-1]

datos = pd.read_csv(files[-1],encoding='utf-8', parse_dates=['DATE'])
datos = datos.fillna(0)

datos = datos.loc[datos['Precio Gasolina 95 Proteccion']>0]
datos = datos.loc[datos['Latitud']!=0]
datos = datos.loc[datos['Longitud (WGS84)']!=0]
datos = datos.loc[datos.Provincia=='MADRID']

datos1 = datos.loc[datos['Precio Gasolina 95 Proteccion'] < datos['Precio Gasolina 95 Proteccion'].quantile(0.25)]
datos2 = datos.loc[datos['Precio Gasolina 95 Proteccion'] >= datos['Precio Gasolina 95 Proteccion'].quantile(0.25)]
datos2 = datos2.loc[datos2['Precio Gasolina 95 Proteccion'] < datos['Precio Gasolina 95 Proteccion'].quantile(0.75)]
datos3 = datos.loc[datos['Precio Gasolina 95 Proteccion'] >= datos['Precio Gasolina 95 Proteccion'].quantile(0.75)]

Precio = datos['Precio Gasolina 95 Proteccion'].astype(str).tolist()
Precio1 = datos1['Precio Gasolina 95 Proteccion'].astype(str).tolist()
Precio2 = datos2['Precio Gasolina 95 Proteccion'].astype(str).tolist()
Precio3 = datos3['Precio Gasolina 95 Proteccion'].astype(str).tolist()

Lat = datos['Latitud'].tolist()
Lat1 = datos1['Latitud'].tolist()
Lat2 = datos2['Latitud'].tolist()
Lat3 = datos3['Latitud'].tolist()

Lon = datos['Longitud (WGS84)'].tolist()
Lon1 = datos1['Longitud (WGS84)'].tolist()
Lon2 = datos2['Longitud (WGS84)'].tolist()
Lon3 = datos3['Longitud (WGS84)'].tolist()

Rotulo = datos['Rotulo'].tolist()
Rotulo1 = datos1['Rotulo'].tolist()
Rotulo2 = datos2['Rotulo'].tolist()
Rotulo3 = datos3['Rotulo'].tolist()

for item in range(len(Rotulo1)):
    Rotulo1[item] = Rotulo1[item] + ' ' + Precio1[item]

for item in range(len(Rotulo2)):
    Rotulo2[item] = Rotulo2[item] + ' ' + Precio2[item]

for item in range(len(Rotulo3)):
    Rotulo3[item] = Rotulo3[item] + ' ' + Precio3[item]

del datos
del datos1
del datos2
del datos3

# create empty map zoomed in on Madrid
map = folium.Map(location=SF_COORDINATES, zoom_start=10)
marker_cluster = MarkerCluster().add_to(map)
marker_cluster2 = MarkerCluster().add_to(map)
marker_cluster3 = MarkerCluster().add_to(map)

for i in range(len(Rotulo1)-1):
#for i in range(len(Rotulo1[:MAX_RECORDS])):
    folium.Marker(icon=folium.Icon(color='green'),popup=folium.Popup(Rotulo1[i], parse_html=True),
        location = (Lat1[i],Lon1[i])).add_to(marker_cluster)

for i in range(len(Rotulo2)-1):
#for i in range(len(Rotulo2[:MAX_RECORDS])):
    folium.Marker(icon=folium.Icon(color='blue'),popup=folium.Popup(Rotulo2[i], parse_html=True),
        location = (Lat2[i],Lon2[i])).add_to(marker_cluster2)

for i in range(len(Rotulo3)-1):
#for i in range(len(Rotulo3[:MAX_RECORDS])):
    folium.Marker(icon=folium.Icon(color='red'),popup=folium.Popup(Rotulo3[i], parse_html=True),
        location = (Lat3[i],Lon3[i])).add_to(marker_cluster3)


os.chdir('/Volumes/MacintoshHD/_Github/gas')
map.save('index.html')
