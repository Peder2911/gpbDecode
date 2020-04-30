from decode import decode
import sqlite3
import geopandas as gpd

con = sqlite3.connect("ne.gpkg")
c = con.cursor()

c.execute("SELECT geom FROM out")
r = c.fetchall()
row = r[0]
b = row[0]

decode(b)
