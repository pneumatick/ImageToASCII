from PIL import Image
import sys
import os.path

A_STRING = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkh"
"ao*#MW&8%B@$"

try:
    im = Image.open(sys.argv[1])
except:
    print("An error occured... Missing file name argument?")
    exit()
else:
    print("Successfully loaded image!\nImage size:", im.size)

w = im.width
h = im.height

# Create two dimensional arrays (matrices)
rgb_matrix = [[0] * h for i in range(w)]
brightness_matrix = [[0] * h for i in range(w)]
ascii_matrix = [[0] * h for i in range(w)]

# Populate RGB matrix with pixel data (tuples)
print("Extracting pixel data...")

for x in range(w):
    for y in range(h):
        rgb_matrix[x][y] = im.getpixel((x, y))
im.close()

# Populate brightness matrix (average of elements of tuple)
print("Calculating brightness...")

for x in range(w):
    for y in range(h):
        pixel = rgb_matrix[x][y]
        brightness_matrix[x][y] = (pixel[0] + pixel[1] + pixel[2]) / 3

# Populate ASCII matrix (corresponding ASCII characters)
print("Selecting ASCII characters...")

for x in range(w):
    for y in range(h):
        ascii_matrix[x][y] = A_STRING[int(brightness_matrix[x][y] / len(A_STRING))]

# Display ASCII text
#for y in range(h):
#    row = ""
#    for x in range(w):
#        row += ascii_matrix[x][y]
#    print(row)

# Format the text file name
print("Generating file name...")

file_name = sys.argv[1].split('\\')[-1]
file_extension = file_name.split('.')[1]
file_name = file_name[:len(file_name) - len(file_extension)] + "txt"

# Write the ASCII text to the file
print("Writing to file...")


f = open(file_name, 'w')
for y in range(h):
    for x in range(w):
        f.write(ascii_matrix[x][y])
    f.write('\n')
f.close()

print("Write successful!")
