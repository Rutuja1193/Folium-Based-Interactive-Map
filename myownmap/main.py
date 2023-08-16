import folium
from folium import plugins
#import geocoder
#import geopy
#import pandas as pd
from folium.plugins import LocateControl, SideBySideLayers


m = folium.Map(location=[48.856974619186985, 2.348662360226061], zoom_start=12)


#m.fit_bounds([[48.856974619186985, 2.348662360226061], [48.856974619186985, -2.348662360226061]])

#tourism
folium.Marker([48.85891912156463, 2.294446167725308],
              popup="<h1> Eiffel Tower</h1><img src='eft.jpg' width=400px><p>Gustave Eiffel's iconic, wrought-iron 1889 tower, with steps and elevators to observation decks. </p>",
              tooltip='Eiffel Tower',
              icon=folium.Icon(icon='camera', icon_color='white', color='blue')).add_to(m)

folium.Marker([48.84614046746433, 2.355615649235953],
              popup="<h1> Grande Galerie de I'Evolution</h1><img src='grande.jpg' width=400px><p>More than 7000 preserved animal specimens displayed in a vast metal & glass 19th-century hall. </p>",
              tooltip='Gallery of Evolution',
              icon=folium.Icon(icon='camera', icon_color='white', color='blue')).add_to(m)

folium.Marker([48.86568002936441, 2.336732899736825],
              popup="<h1>Louvre Pyramid </h1><img src='louvre.jpg' width=400px><p>Glass pyramid created by I. M. Pei, forming the entraceway into a lower-ground exhibition area. </p>",
              tooltip='Louvre Pyramid',
              icon=folium.Icon(icon='camera', icon_color='white', color='blue')).add_to(m)

folium.Marker([48.860570276491856, 2.34410259284584],
              popup="<h1>Sainte-Chapelle </h1><img src='sainte.jpg' width=400px><p>Ornate, 13th-century, Gothic chapel with relics & notable stained-glass windows of bibical scenes. </p>",
              tooltip='Sainte-Chapelle',
              icon=folium.Icon(icon='camera', icon_color='white', color='blue')).add_to(m)

folium.Marker([48.87276576343035, 2.317151756161392],
              popup="<h1>Jardin des Champs-Elysees </h1><img src='jardin.jpg' width=400px><p>Iconic formal gardens landscaped by Andre Le Notre in 1667, with theaters, palaces & statues. </p>",
              tooltip='Jardin des Champs-Elysees',
              icon=folium.Icon(icon='camera', icon_color='white', color='blue')).add_to(m)

#restaurants
folium.Marker([48.857365799520664, 2.3374076331608125],
              popup="<h1>Lobineau </h1><img src='lobineau.jpg' width=400px><p>Intimate bistro with sidewalk seating offering traditional dishes spotlighting seafood. </p>",
              tooltip='Lobineau',
              icon=folium.Icon(icon='cutlery', icon_color='black', color='orange')).add_to(m)

folium.Marker([48.831734473779626, 2.371362160167213],
              popup="<h1>Arlocchino </h1><img src='arlocchino.JPG' width=400px><p>A real delight with homemade sauces and desserts. </p>",
              tooltip='Arlocchino',
              icon=folium.Icon(icon='cutlery', icon_color='black', color='orange')).add_to(m)

folium.Marker([48.878142843777034, 2.3532004791542893],
              popup="<h1>Old Shalimar </h1><img src='old shalimar.jpg' width=400px><p>Meat, fish & vegetarian curries fixed up in an unpretentious restaurant with a sidewalk terrace. </p>",
              tooltip='Old Shalimar',
              icon=folium.Icon(icon='cutlery', icon_color='black', color='orange')).add_to(m)

folium.Marker([48.84395354197944, 2.344029291923241],
              popup="<h1>Bistronomique Florina </h1><img src='florina.jpg' width=400px><p>Cuisine elaborated with fresh products, homemade and with a gastronomic touch. </p>",
              tooltip='Bistronomique Florina',
              icon=folium.Icon(icon='cutlery', icon_color='black', color='orange')).add_to(m)

folium.Marker([48.85904169210472, 2.3615605601672134],
              popup="<h1>Le Chanard </h1><img src='le chanard.jpg' width=400px><p>Intimate venue with a small terrace & cozy interiors, offering classic french food. </p>",
              tooltip='Le Chanard',
              icon=folium.Icon(icon='cutlery', icon_color='black', color='orange')).add_to(m)

#hospital
folium.Marker([48.83342661267628, 2.3133893273845216],
              popup="<h1>Saint-Joseph Hospital </h1><p> </p>",
              tooltip='Saint-Joseph Hospital',
              icon=folium.Icon(icon='header', icon_color='white', color='red')).add_to(m)

folium.Marker([48.844273070205595, 2.3607678666072314],
              popup="<h1>Salpetriere Hospital </h1><img src='sal.jpeg' width=400px><p> </p>",
              tooltip='Salpetriere Hospital',
              icon=folium.Icon(icon='header', icon_color='white', color='red')).add_to(m)

folium.Marker([48.884136203896404, 2.377419020612388],
              popup="<h1>Foundation Adolphe de Rothschild Hospital </h1><p> </p>",
              tooltip='Foundation Adolphe de Rothschild Hospital',
              icon=folium.Icon(icon='header', icon_color='white', color='red')).add_to(m)

folium.Marker([48.88774828942138, 2.3049779207863685],
              popup="<h1>Clinique International Hospital </h1><p> </p>",
              tooltip='Clinique International Hospital',
              icon=folium.Icon(icon='header', icon_color='white', color='red')).add_to(m)

folium.Marker([48.878261220977414, 2.3699415601672134],
              popup="<h1>Saint-Louis Hospital </h1><p> </p>",
              tooltip='Saint-Louis Hospital',
              icon=folium.Icon(icon='header', icon_color='white', color='red')).add_to(m)

#atms
folium.Marker([48.84368177605798, 2.3238743284111854],
              popup="<h1>Societe Generale ATM </h1><p> </p>",
              tooltip='Societe Generale ATM',
              icon=folium.Icon(icon='euro', icon_color='black', color='blue')).add_to(m)

folium.Marker([48.84099365522694, 2.352689475865048],
              popup="<h1>ATM </h1><p> </p>",
              tooltip='ATM',
              icon=folium.Icon(icon='euro', icon_color='black', color='blue')).add_to(m)

folium.Marker([48.89519426631659, 2.3187005238139733],
              popup="<h1>GAB BNP Paribas ATM </h1><p> </p>",
              tooltip='GAB BNP Paribas ATM',
              icon=folium.Icon(icon='euro', icon_color='black', color='blue')).add_to(m)

folium.Marker([48.87318234923149, 2.291749687055564],
              popup="<h1>ATM </h1><p> </p>",
              tooltip='ATM',
              icon=folium.Icon(icon='euro', icon_color='black', color='blue')).add_to(m)

#pharmacy
folium.Marker([48.86335851262067, 2.3544060886271723],
              popup="<h1>Archives Pharmacy </h1><p> </p>",
              tooltip='Archives Pharmacy',
              icon=folium.Icon(icon='plus', icon_color='red', color='green')).add_to(m)

folium.Marker([48.89564568282913, 2.343076437943481],
              popup="<h1>Custin well & well Pharmacy </h1><p> </p>",
              tooltip='Custin well & well Pharmacy',
              icon=folium.Icon(icon='plus', icon_color='red', color='green')).add_to(m)

folium.Marker([48.88255269952838, 2.3537194431311907],
              popup="<h1>Central North Pharmacy </h1><p> </p>",
              tooltip='Central North Pharmacy',
              icon=folium.Icon(icon='plus', icon_color='red', color='green')).add_to(m)

folium.Marker([48.86990794520091, 2.2823083108747584],
              popup="<h1>Lafayette Pharmacy </h1><p> </p>",
              tooltip='Lafayette Pharmacy',
              icon=folium.Icon(icon='plus', icon_color='red', color='green')).add_to(m)

folium.Marker([48.85089778468734, 2.4042063237308953],
              popup="<h1>Pharmacy Marsoulan </h1><p> </p>",
              tooltip='Pharmacy Marsoulan',
              icon=folium.Icon(icon='plus', icon_color='red', color='green')).add_to(m)

#colleges
folium.Marker([48.86665251235251, 2.3091928464272597],
              popup="<h1>The American University of Paris </h1><img src='amer.jpeg' width=400px><p>Private University </p>",
              tooltip='The American University of Paris',
              icon=folium.Icon(icon='pencil', icon_color='red', color='blue')).add_to(m)

folium.Marker([48.85464459481213, 2.3446312919232413],
              popup="<h1>College de France </h1><img src='france.JPG' width=400px><p>Unique education & research institution with diverse lectures from a changing roster of experts. </p>",
              tooltip='College de France',
              icon=folium.Icon(icon='pencil', icon_color='red', color='blue')).add_to(m)

folium.Marker([48.87952269854874, 2.297293714671232],
              popup="<h1>Schiller International University </h1><img src='schiller.jpg' width=400px><p>Private University that offers Bachelor and Master degrees, with its main campus and administrative headquaters in Florida. Campus resources include a computer lab, a student lounge and many facilities. Students may also have access to the American Library of Paris. </p>",
              tooltip='Schiller International University',
              icon=folium.Icon(icon='pencil', icon_color='red', color='blue')).add_to(m)

folium.Marker([48.848003056881204, 2.3905016464272597],
              popup="<h1>Middle School Sainte-Clotilde </h1><img src='clotilde.jpeg' width=400px><p>Middle School </p>",
              tooltip='Middle School Sainte-Clotilde',
              icon=folium.Icon(icon='pencil', icon_color='red', color='blue')).add_to(m)

folium.Marker([48.88297215493656, 2.364934623679269],
              popup="<h1>College la Grange Aux Belles </h1><img src='belles.jpeg' width=400px><p>Middle School </p>",
              tooltip='College la Grange Aux Belles',
              icon=folium.Icon(icon='pencil', icon_color='red', color='blue')).add_to(m)

#malls
folium.Marker([48.89318011088881, 2.237685152831597],
              popup="<h1>Westfield les 4 temps </h1><img src='west.jpg' width=400px><p>Shopping mall with the biggest brands all together for you! </p>",
              tooltip='Westfield les 4 temps',
              icon=folium.Icon(icon='shopping-cart', icon_color='white', color='green')).add_to(m)

folium.Marker([48.85385865961198, 2.2821896374192225],
              popup="<h1>Centre Commercial Beaugrenelle </h1><img src='centre.jpg' width=400px><p>Elegant enclosed mall featuring upscale global brand on multiple floors, plus eateries & a cinema. </p>",
              tooltip='Centre Commercial Beaugrenelle',
              icon=folium.Icon(icon='shopping-cart', icon_color='white', color='green')).add_to(m)

folium.Marker([48.8709627709076, 2.341588511376022],
              popup="<h1>Galerie Vivienne </h1><img src='galerie.jpg' width=400px><p>Covered mall built in 1823 to plans by architect Francois-Jean Delanno & now housing luxury shops. </p>",
              tooltip='Galerie Vivienne',
              icon=folium.Icon(icon='shopping-cart', icon_color='white', color='green')).add_to(m)

folium.Marker([48.87598171345409, 2.307797851159176],
              popup="<h1>Galeries Lafayette Champs-Élysées </h1><img src='lafayette.jpg' width=400px><p>Choose from a wide selection of clothing for men, women and children. Come and discover the Galaries Lafayette Paris and enjoy exclusive advantages with our loyalty program. </p>",
              tooltip='Galeries Lafayette Champs-Élysées',
              icon=folium.Icon(icon='shopping-cart', icon_color='white', color='green')).add_to(m)

folium.Marker([48.853063099517655, 2.323649896066157],
              popup="<h1>Le Bon Marché </h1><img src='marhe.jpg' width=400px><p>Upmarket 19th-century mall for designer apparel, housewares, beauty products & gourmet groceries.  </p>",
              tooltip='Le Bon Marché',
              icon=folium.Icon(icon='shopping-cart', icon_color='white', color='green')).add_to(m)
wms_url = 'http://ows.mundialis.de/services/service?'
layer_n='OSM-WMS'
url = 'https://ows.terrestris.de/osm/service?'
layer_name = 'OSM-WMS'
image_url = 'jardin.jpg'
image_bounds = [[49.712216, 2.22655], [49.773941, 2.12544]]


# add tiles to map
folium.raster_layers.TileLayer('Open Street Map').add_to(m)
folium.raster_layers.TileLayer('Stamen Terrain').add_to(m)
folium.raster_layers.TileLayer('Stamen Toner').add_to(m)
folium.raster_layers.TileLayer('Stamen Watercolor').add_to(m)
folium.raster_layers.TileLayer('CartoDB Positron').add_to(m)
folium.raster_layers.TileLayer('CartoDB Dark_Matter').add_to(m)
#folium.raster_layers.ImageOverlay(image_url,bounds=image_bounds, opacity=0.6).add_to(m)
folium.raster_layers.WmsTileLayer(url,layers=layer_name,fmt='image/jpeg', transparent=False, version='1.1.1', attr="Weather data © 2023 IEM Nexrad", name='WMS', overlay=True, control=True, show=True).add_to(m)
folium.raster_layers.WmsTileLayer(wms_url,layers=layer_n,fmt='image/jpeg', transparent=False, version='1.1.1', attr="Weather data © 2023 IEM Nexrad", name='WMS2', overlay=True, control=True, show=True).add_to(m)
#folium.raster_layers.VideoOverlay('https://www.youtube.com/watch?v=dQw4w9WgXcQ',[[48.856974619186985, 2.348662360226061], [48.856974619186985, 2.348662360226061]],autoplay=True, loop=True, name=None, overlay=True, control=True, show=True).add_to(m)

#olium.LayerControl().add_to(m)
minimap = plugins.MiniMap(toggle_display=True)

# add minimap to map
m.add_child(minimap)

# add scroll zoom toggler to map
plugins.ScrollZoomToggler().add_to(m)

# add full screen button to map
plugins.Fullscreen(position='topright').add_to(m)

m.add_child(folium.LatLngPopup())


draw = plugins.Draw()

# add draw tools to map
draw.add_to(m)

LocateControl().add_to(m)



measure_control = plugins.MeasureControl(position='topleft',
                                         active_color='red',
                                         completed_color='red',
                                         primary_length_unit='meters')



folium.JavascriptLink("https://unpkg.com/leaflet-control-geocoder/dist/Control.Geocoder.js")
# add measure control to map
m.add_child(measure_control)
folium.LayerControl().add_to(m)
m.save('map.html')


