import folium
from folium import LayerControl, Marker
from folium.plugins import DualMap

#DualMap accepts the same arguments as Map:
m = DualMap(location=(0, 0), tiles="cartodbpositron", zoom_start=5)
# Add the same marker to both maps:
Marker((0, 0)).add_to(m)
# The individual maps are attributes called `m1` and `m2`:
Marker((0, 1)).add_to(m.m1)
LayerControl().add_to(m)
fg = folium.FeatureGroup()  # Main group
g1 = folium.plugins.FeatureGroupSubGroup(fg, "g1")  # First subgroup of fg
g2 = folium.plugins.FeatureGroupSubGroup(fg, "g2")  # Second subgroup of fg
m.add_child(fg)
m.add_child(g1)
m.add_child(g2)
g1.add_child(folium.Marker([0, 0]))
g2.add_child(folium.Marker([0, 1]))
folium.LayerControl().add_to(m)
mcg = folium.plugins.MarkerCluster(
    control=False
)  # Marker Cluster, hidden in controls
g1 = folium.plugins.FeatureGroupSubGroup(mcg, "g1")  # First group, in mcg
g2 = folium.plugins.FeatureGroupSubGroup(mcg, "g2")  # Second group, in mcg
m.add_child(mcg)
m.add_child(g1)
m.add_child(g2)
g1.add_child(folium.Marker([0, 0]))
g2.add_child(folium.Marker([0, 1]))
folium.LayerControl().add_to(m)


m.save("map2.html")

