import os
from PIL import Image

for f in os.listdir('.'):
    if f.endswith('.png'):
        i = Image.open(f)
        fn, fe = os.path.splitext(f)
        i.thumbnail((300,300))
        i.save(f'pngs/{fn}{fe}')
