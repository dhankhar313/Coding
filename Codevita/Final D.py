from scipy import ndimage

rotated = ndimage.rotate('data\\smarties.png', 45)
print(rotated)
