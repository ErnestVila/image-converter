import sys
import os
from PIL import Image

# Garb the first and second argument
path = sys.argv[1]
directory = sys.argv[2]

# Check if /new exists, if not create it
if not os.path.exists(directory):
    os.makedirs(directory)

# Loop throug pokedex
# Convert images to PNG
# Save to the new folder
for filename in os.listdir(path):
    clean_name = os.path.splitext(filename)[0]
    img = Image.open(f'{path}{filename}')
    # added the / in case user doesn't enter it. You may want to check for this and add or remover it.
    img.save(f'{directory}/{clean_name}.png', 'png')
    print('all done!')
