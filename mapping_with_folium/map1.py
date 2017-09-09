import folium
import pandas

data=pandas.read_csv("Volcanoes.txt")
lat=list(data["LAT"]) #latitude
lon=list(data["LON"]) #longtitude
elev=list(data["ELEV"]) #elevation

def colorByHeight(elev):  #marker color by height
    if elev<1000:
        return "blue"
    elif  1000<elev<2000:
        return "green"
    else:
        return "red"

map=folium.Map(location=[38.58,-97.09],zoom_start=5) #map creation

featureGroup=folium.FeatureGroup(name="Map") # add a feature group

for lt,ln,el in zip(lat,lon,elev):
  featureGroup.add_child(folium.Marker(location=[lt,ln],popup=str(el)+" meters",icon=folium.Icon(color=colorByHeight(el)))) #markers creator

featureGroup.add_child(folium.GeoJson(data=(open('world.json','r',encoding='utf-8-sig').read())))

map.add_child(featureGroup)

map.save("map1.html")
