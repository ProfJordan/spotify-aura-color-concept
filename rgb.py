from cs50 import SQL
from PIL import Image

db = SQL("sqlite:///songs.db")

# values as AVGs
# rows = db.execute("SELECT AVG(danceability) AS r, AVG(energy) AS g, AVG(valence) AS b FROM songs")

# values as SUM totals
rows = db.execute("SELECT SUM(danceability) AS r, SUM(energy) AS g, SUM(valence) AS b FROM songs")
row = rows[0]

print(row["r"])
print(row["g"])
print(row["b"])

def convert_to_rgb(r, g, b):
    # Ensure the averages are in the correct range
    # if not (0.00 <= r <= 1.00 and 0.00 <= g <= 1.00 and 0.00 <= b <= 1.00):
    #     raise ValueError("Each of r, g, and b must be between 0.00 and 1.00")

    # Ensure the sums are in the correct range of 0-255
    if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
        # if not round and divide to get the nearest integer
        r_rgb = int(round(r / 255))
        g_rgb = int(round(g / 255))
        b_rgb = int(round(b / 255))

    else:
    # Convert each average vaue by multiplying by 255 and rounding to the nearest integer
    # r_rgb = int(round(r * 255))
    # g_rgb = int(round(g * 255))
    # b_rgb = int(round(b * 255))
    # Convert each SUM total by rounding to nearest integer
        r_rgb = int(round(r))
        g_rgb = int(round(g))
        b_rgb = int(round(b))


    return r_rgb, g_rgb, b_rgb

def create_color_bmp(filename, color, width, height):
    # Create a new image with RGB mode
    image = Image.new('RGB', (width, height), color)

    # Save the image as BMP
    image.save(filename, 'BMP')

r, g, b = row["r"], row["g"], row["b"]
rgb_values = convert_to_rgb(r, g, b)
print("RGB values:", rgb_values)
# create_color_bmp('user-aura-avg.bmp', rgb_values, 100, 100)  # Creates a 100x100 pixel image
create_color_bmp('user-aura-sum.bmp', rgb_values, 100, 100)  # Creates a 100x100 pixel image
print("BMP file created with the specified background color.")
