from PIL import Image, ImageDraw

def main():

    width = 1000
    height = 1000
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    draw.rectangle(((0, 0), (width, height)), fill="white")

# draw a rectangle from x0, y0 to x1, y1
    draw.rectangle(((525, 400), (475, 700)), fill="blue")

# draw a line from x0, y0, x1, y1
# using the color pink
    # color = (256, 128, 128)  # pink
    draw.line((200, 800, 475, 700), fill="blue")
    # draw.line((0, height, width, 0), fill=color)


    circle_x = width/2
    circle_y = height/3
    circle_radius = 100
    draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='blue')

    img.save('im1.png')

main()