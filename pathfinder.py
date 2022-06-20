from re import X
from PIL import Image, ImageDraw, ImageColor


with open("elevation_small.txt") as elevation_text:
    elevation_grid = elevation_text.readlines()
    y_values = len(elevation_grid)
    """ min_elevation = min(y)
    max_elevation = max(y)"""

    def number_lines(i):
        for i in range(0, 599):
            i += 1
            y = elevation_grid[i].split()
            elevation_dict = {str(key): y[key] for key in range(0, 600)}
            assign_color_values(elevation_dict)
            print(f"List Number {i}: List: {y}")
    # here i want to make a function where i can iterate through dictionaries by making y(line) = elevation_grid(line).split()

    """y1 = elevation_grid[0].split()
    min_elevation1 = min(y1)
    max_elevation1 = max(y1)"""
    # elevation_dict0 = {str(key): y1[key] for key in range(0, len(y1))}
    map = Image.new("RGBA", (600, 600), "white")

    def assign_color_values(elevation_dict):
        for key, value in elevation_dict.items():
            if key <= ("599"):
                x = f"{key}"
                value = int(value)
                if value >= 3859 and value <= 3899:
                    color_code = 1
                    if color_code == 1:
                        map.putpixel((x, y), (0, 0, 0, 0))
                    # map.putpixel((x, 1), (220, 220, 220, 220))
                if value >= 3900 and value <= 3999:
                    color_code = 2
                    if color_code == 2:
                        map.putpixel((x, y), (10, 10, 10, 10))
                if value >= 4000 and value <= 4099:
                    color_code = 3
                if value >= 4100 and value <= 4199:
                    color_code = 4
                if value >= 4200 and value <= 4299:
                    color_code = 5
                if value >= 4300 and value <= 4399:
                    color_code = 6
                if value >= 4400 and value <= 4499:
                    color_code = 7
                if value >= 4500 and value <= 4599:
                    color_code = 8
                if value >= 4600 and value <= 4699:
                    color_code = 9
                if value >= 4700 and value <= 4799:
                    color_code = 10
                if value >= 4800 and value <= 4899:
                    color_code = 11
                if value >= 4900 and value <= 4999:
                    color_code = 12
                if value >= 5000 and value <= 5099:
                    color_code = 13
                if value >= 5100 and value <= 5199:
                    color_code = 14
                if value >= 5200 and value <= 5299:
                    color_code = 15
                elif value >= 5300 and value <= 5399:
                    color_code = 16
            print(f"({x}x, 1y)")
            print(f"Color Code:{color_code} | Elevation: {value}")

    def put_colors():
        for x in range(599):
            y = 1

            if color_code == 3:
                map.putpixel((x, y), (50, 50, 50, 50))
            if color_code == 4:
                map.putpixel((x, y), (70, 70, 70, 70))
            if color_code == 5:
                map.putpixel((x, y), (90, 90, 90, 90))
            if color_code == 6:
                map.putpixel((x, y), (110, 110, 110, 110))
            if color_code == 7:
                map.putpixel((x, y), (125, 125, 125, 125))
            if color_code == 8:
                map.putpixel((x, y), (140, 140, 140, 140))
            if color_code == 9:
                map.putpixel((x, y), (155, 155, 155, 155))
            if color_code == 10:
                map.putpixel((x, y), (170, 170, 170, 170))
            if color_code == 11:
                map.putpixel((x, y), (185, 185, 185, 185))
            if color_code == 12:
                map.putpixel((x, y), (200, 200, 200, 200))
            if color_code == 13:
                map.putpixel((x, y), (210, 210, 210, 210))
            if color_code == 14:
                map.putpixel((x, y), (220, 220, 220, 220))
            if color_code == 15:
                map.putpixel((x, y), (230, 230, 230, 230))
            if color_code == 16:
                map.putpixel((x, y), (240, 240, 240, 240))
            # technically y = numList + 1
            # this is because y= 0 on a graph is directly on the x axis
        map.save("map2.png")
        print(color_code)
    assign_color_values(elevation_dict)
    put_colors()
