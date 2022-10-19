import json
from shapely.geometry import asShape, mapping


def main():
    """
    気象庁における地震情報細分区域ごとにgeojsonファイルを出力
    """
    file = "./area/geojson/output.geojson"

    with open(file) as f:
        data = f.read()

    areas = json.loads(data)

    # 区分コードごとにファイル出力
    for area in areas["features"]:
        properties = area["properties"]
        code = properties["code"]
        geometry = asShape(area["geometry"])
        simply_geo = mapping(geometry.simplify(0.001))

        geojson = {
            "type": "FeatureCollection",
            "features": [{
                "type": "Feature",
                "properties": properties,
                "geometry": simply_geo
            }]
        }

        with open(f"./area/geojson/{code}.geojson", "w") as out_file:
            json.dump(geojson, out_file)


if __name__ == '__main__':
    main()