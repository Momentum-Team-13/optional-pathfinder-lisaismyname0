from re import X
from PIL import Image, ImageDraw, ImageColor

with open("elevation_small.txt") as elevation_text:
    elevation_grid = elevation_text.readlines()
    x1 = elevation_grid[0].split()
    y_values = len(elevation_grid)
    x_values = len(x1)
    min_elevation1 = min(x1)
    max_elevation1 = max(x1)
    elevation_dict1 = {str(key): x1[key] for key in range(0, len(x1))}
    map = Image.new("RGBA", (600, 600), "white")
    for key, value in elevation_dict1.items():
        if key <= ("599"):
            x = f"{key}"
            value = int(value)
            if value >= 3859 and value <= 3899:
                color_code = 1
                print(f"({x}x, 1y)")
                print(f"Color Code:{color_code} | Elevation: {value}")
            if value >= 3900 and value <= 3999:
                color_code = 2
                print(f"({x}x, 1y)")
                print(f"Color Code:{color_code} | Elevation: {value}")
            if value >= 4000 and value <= 4099:
                color_code = 3
                print(f"({x}x, 1y)")
                print(f"Color Code:{color_code} | Elevation: {value}")
            if value >= 4100 and value <= 4199:
                color_code = 4
                print(f"({x}x, 1y)")
                print(f"Color Code:{color_code} | Elevation: {value}")
            if value >= 4200 and value <= 4299:
                color_code = 5
                print(f"({x}x, 1y)")
                print(f"Color Code:{color_code} | Elevation: {value}")
            if value >= 4300 and value <= 4399:
                color_code = 6
                print(f"({x}x, 1y)")
                print(f"Color Code:{color_code} | Elevation: {value}")
            if value >= 4400 and value <= 4499:
                color_code = 7
                print(f"({x}x, 1y)")
                print(f"Color Code:{color_code} | Elevation: {value}")
            if value >= 4500 and value <= 4599:
                color_code = 8
                print(f"({x}x, 1y)")
                print(f"Color Code:{color_code} | Elevation: {value}")
            if value >= 4600 and value <= 4699:
                color_code = 9
            if value >= 4700 and value <= 4799:
                color_code = 10
                print(f"({x}x, 1y)")
                print(f"Color Code:{color_code} | Elevation: {value}")
            if value >= 4800 and value <= 4899:
                color_code = 11
                print(f"({x}x, 1y)")
                print(f"Color Code:{color_code} | Elevation: {value}")
            if value >= 4900 and value <= 4999:
                color_code = 12
                print(f"({x}x, 1y)")
                print(f"Color Code:{color_code} | Elevation: {value}")
            if value >= 5000 and value <= 5099:
                color_code = 13
            if value >= 5100 and value <= 5199:
                color_code = 14
                print(f"({x}x, 1y)")
                print(f"Color Code:{color_code} | Elevation: {value}")
            if value >= 5200 and value <= 5299:
                color_code = 15
                print(f"({x}X, 1Y)")
                print(f"Color Code:{color_code} | Elevation: {value}")
            elif value >= 5300 and value <= 5399:
                color_code = 16
    print(map.getpixel((1, 1)))
    print(map.getpixel((0, 0)))
    map.save("map2.png")
