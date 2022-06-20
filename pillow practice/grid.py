grid_row = []
for i in range(5):
    grid_row.append("")
grid = []
for i in range(5):
    grid.append(list(grid_row))

    for key, value in elevation_dict1.items():
        if key <= ("599"):
            if value >= 3859 and value <= 3899:
                color_code = int(1)
                print(color_code)
            if value >= 3900 and value <= 3999:
                color_code = 2
                print(color_code)
            if value >= 4000 and value <= 4099:
                color_code = 3
                print(color_code)
            if value >= 4100 and value <= 4199:
                color_code = 4
                print(color_code)
            if value >= 4200 and value <= 4299:
                color_code = 5
                print(color_code)
            if value >= 4300 and value <= 4399:
                color_code = 6
                print(color_code)
            if value >= 4400 and value <= 4499:
                color_code = 7
                print(color_code)
            if value >= 4500 and value <= 4599:
                color_code = 8
                print(color_code)
            if value >= 4600 and value <= 4699:
                color_code = 9
            if value >= 4700 and value <= 4799:
                color_code = 10
                print(color_code)
            if value >= 4800 and value <= 4899:
                color_code = 11
                print(color_code)
            if value >= 4900 and value <= 4999:
                color_code = 12
                print(color_code)
            if value >= 5000 and value <= 5099:
                color_code = 13
            if value >= 5100 and value <= 5199:
                color_code = 14
                print(color_code)
            if value >= 5200 and value <= 5299:
                color_code = 15
                print(color_code)
            elif value >= 5300 and value <= 5399:
                color_code = 16
                print(color_code)

    y1 = elevation_grid[0].split()
    y_values = len(elevation_grid)
    x_values = len(y1)
    min_elevation1 = min(y1)
    max_elevation1 = max(y1)
    elevation_dict0 = {str(key): y1[key] for key in range(0, len(y1))}