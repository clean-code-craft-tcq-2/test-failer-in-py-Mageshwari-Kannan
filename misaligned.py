major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]


def color_mapping():
    cp_rows = []

    for i, major_color in enumerate(major_colors):
        for j, minor_color in enumerate(minor_colors):
            print_color_map((i * 5 + j)+1 , major_color, minor_color)
            cp_rows.append(f'{(i * 5 + j)+1} | {major_color} | {minor_color}')

    return len(major_colors) * len(minor_colors), cp_rows

def print_color_map(pair_number, major_color, minor_color):
    print(f'{pair_number} | {major_color} | {minor_color}')
  

result, cp_rows = color_mapping()

assert (cp_rows[3] == '4 | White | Brown')
assert (cp_rows[7] == '8 | Red | Green')
assert (cp_rows[23] == '24 | Violet | Brown')
print("All is well (maybe!)\n")
