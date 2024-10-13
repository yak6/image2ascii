from PIL import Image
# ██
char = "██" 

path = "opensource.bmp"

colors = {
    '\033[30m': (0, 0, 0),
    '\033[31m': (255, 0, 0),
    '\033[32m': (0, 255, 0),
    '\033[33m': (255, 255, 0),
    '\033[34m': (0, 0, 255),
    '\033[35m': (255, 0, 255),
    '\033[36m': (0, 255, 255),
    '\033[37m': (255, 255, 255),
    '\033[90m': (169, 169, 169),  
    '\033[91m': (255, 102, 102),   
    '\033[92m': (102, 255, 102),  
    '\033[93m': (255, 255, 102),
    '\033[94m': (102, 102, 255),   
    '\033[95m': (255, 102, 255),
    '\033[96m': (102, 255, 255),    
    '\033[97m': (255, 255, 255),  
}

previous_y = -1

def get_closest_color(color):
    r, g, b = color
    min_distance = float('inf')
    closest_color = None

    for color_name, rgb in colors.items():
        distance = ((r - rgb[0]) ** 2 + (g - rgb[1]) ** 2 + (b - rgb[2]) ** 2) ** 0.5
        if distance < min_distance:
            min_distance = distance
            closest_color = color_name

    return closest_color

def read_image(file_path):
    image = Image.open(file_path)

    if image.mode not in ['RGB', 'RGBA']:
        image = image.convert('RGB')

    color_map = {}

    for y in range(image.height):
        for x in range(image.width):
            r, g, b = image.getpixel((x, y))[:3]
            color_map[(x, y)] = (r, g, b)

    return color_map

color_map = read_image(path)

for position, color in color_map.items():
    current_y = position[1]  

    if current_y != previous_y:
        if previous_y != -1:
            print()  
        previous_y = current_y  

    print(f"{get_closest_color(color)}{char}", end='')

print("\033[0m")
