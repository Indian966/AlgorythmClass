from PIL import Image


def convert_grayscale(image):
    width, height = image.size

    new_image = Image.new("RGB", (width, height), "white")
    for i in range(width):
        for j in range(height):
            pixel = image.getpixel((i, j))
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]
            gray = (red * 0.299) + (green * 0.587) + (blue * 0.114)
            new_image.putpixel((i, j), (int(gray), int(gray), int(gray)))
    return new_image


original = Image.open('./dice.png')

output = convert_grayscale(original)

output.show()