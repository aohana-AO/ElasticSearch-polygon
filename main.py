import geopandas as gpd
import matplotlib
from matplotlib import pyplot
from shapely.geometry import Point
import pyproj
import pandas as pd
import numpy as np
import re

#geojsonの読み込み
geo_path461 = 'geojson/461.geojson'
geo_path462 = 'geojson/462.geojson'
geo_path551 = 'geojson/551.geojson'
geodate = gpd.read_file(geo_path461, encoding='UTF-8')
geodate2 = gpd.read_file(geo_path462, encoding='UTF-8')
geodate3 = gpd.read_file(geo_path551, encoding='UTF-8')

#geojsonの追加
geodate = geodate.append(geodate2)
geodate = geodate.append(geodate3)

#列jisintiikiでマルチpolygon化

geodate['jisinntiiki']='jisinn'
'''
#列を少なくする
geodate = geodate[['jisinntiiki','geometry']]
'''

geodatemulti = geodate.dissolve(by='jisinntiiki')
'''
#列を少なくする
geodatemulti = geodatemulti[['code','name','namekana','geometry']]
'''

print(geodatemulti)
path='multi2.geojson'
geodatemulti.to_file(path, driver="GeoJSON")

#プロット
geodatemulti.plot()
pyplot.show()

