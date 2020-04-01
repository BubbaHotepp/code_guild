from PIL import Image, ImageDraw

def main():

    width = 1000
    height = 1000
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    draw.rectangle(((0, 0), (width, height)), fill='white')
    draw.rectangle(((525, 400), (475, 700)), fill='blue')
    draw.rectangle((350, 550, 650, 500), fill='blue')
    draw.rectangle((400, 700, 600, 750), fill='blue')
    draw.rectangle((600, 700, 650, 900), fill='blue')
    draw.rectangle((350, 700, 400, 900), fill='blue')
    circle_x = width/2
    circle_y = height/3
    circle_radius = 100
    draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='blue')

    img.show()

main()