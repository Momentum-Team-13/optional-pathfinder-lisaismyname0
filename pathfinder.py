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
    for num in elevation_dict1.values():
        # here I color code all of the values within my dictionary
        num = int(num)
        if num >= 3859 and num <= 3899:
            color_code = 1
            # print(f"{num}'s color code is {color_code}")
        if num >= 3900 and num <= 3999:
            color_code = 2
            # print(f"{num}'s color code is {color_code}")
        if num >= 4000 and num <= 4099:
            color_code = 3
            # print(f"{num}'s color code is {color_code}")
        if num >= 4100 and num <= 4199:
            color_code = 4
            # print(f"{num}'s color code is {color_code}")
        if num >= 4200 and num <= 4299:
            color_code = 5
            # print(f"{num}'s color code is {color_code}")
        if num >= 4300 and num <= 4399:
            color_code = 6
            # print(f"{num}'s color code is {color_code}")
        if num >= 4400 and num <= 4499:
            color_code = 7
            # print(f"{num}'s color code is {color_code}")
        if num >= 4500 and num <= 4599:
            color_code = 8
            # print(f"{num}'s color code is {color_code}")
        if num >= 4600 and num <= 4699:
            color_code = 9
        if num >= 4700 and num <= 4799:
            color_code = 10
            # print(f"{num}'s color code is {color_code}")
        if num >= 4800 and num <= 4899:
            color_code = 11
            # print(f"{num}'s color code is {color_code}")
        if num >= 4900 and num <= 4999:
            color_code = 12
            # print(f"{num}'s color code is {color_code}")
        if num >= 5000 and num <= 5099:
            color_code = 13
        if num >= 5100 and num <= 5199:
            color_code = 14
            # print(f"{num}'s color code is {color_code}")
        if num >= 5200 and num <= 5299:
            color_code = 15
            # print(f"{num}'s color code is {color_code}")
        elif num >= 5300 and num <= 5399:
            color_code = 16
            # print(f"{num}'s color code is {color_code}")

    map = Image.new("RGBA", (600, 600), "white")
    for key, value in elevation_dict1.items():
        if key <= ("599"):
            x = f"{key}"
            value = int(value)
            if value >= 3859 and value <= 3899:
                color_code = 1
                print(f"Coordinates:({x}x, 1y)")
                print(f"Color Code:{color_code} | Elevation: {value}")
    """for x in range(599):
            if color_code == 1:
                map.putpixel((x, 1), (100, 100, 100))
                print(color_code)
            if color_code == 2:
                map.putpixel(x, 1), (200, 200, 200)
            else:
                break"""
    print(map.getpixel((1, 1)))
    print(map.getpixel((0, 0)))
    map.save("map2.png")
