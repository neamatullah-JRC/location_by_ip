import requests
import folium

res = requests.get('https://ipinfo.io/')
data = res.json()

print(data)
locaion=data['loc'].split(',')
ip = data['ip']

lat=float(locaion[0])
log=float(locaion[1])

fg=folium.FeatureGroup("my map")
fg.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read()))
fg.add_child(folium.Marker(location=[lat,log],popup=ip))
map=folium.Map(location=[lat,log],zoom_start=7)
map.add_child(fg)
map.save("1.html")
if map :
    print("success created map !")

else :
    print("occured error")