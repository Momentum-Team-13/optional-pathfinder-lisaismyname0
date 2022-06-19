with open("elevation_small.txt") as elevation_text:
    elevation_grid = elevation_text.readlines()
    split0 = elevation_grid[0].split()
    min_elevation = min(split0)
    print(min_elevation)
    max_elevation = max(split0)
    print(max_elevation)
    while min_elevation <= max_elevation:
        

    list0_dict = dict.fromkeys(split0, 0)
