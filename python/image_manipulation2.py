import colorsys
from PIL import Image

def main():

    img = Image.open("lenna.png") 
    width, height = img.size
    pixels = img.load()

    for i in range(width):
        for j in range(height):
            (r, g, b) = pixels[i, j]
            h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
            h = h - 0.6
            s = s + 0.1
            v = v - 0.8
            r, g, b = colorsys.hsv_to_rgb(h, s, v)
            r = int(r*255)
            g = int(g*255)
            b = int(b*255)
            pixels[i, j] = (r,g,b)
    
    img.show()

main()