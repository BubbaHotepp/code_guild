# import PIL
from PIL import Image
def main():
    image_input = Image.open('lena.png')
    width, height = image_input.size
    pixels = image_input.load()

    for i in range(width):
        for j in range(height):
            (r, g, b) = pixels[i, j]
            y = 0.299 * float(r) + 0.587 * float(g) + 0.114 * float(b)
            pixels[i, j] = (r, g, b)
            
    image_input.show()

main()

