def resize_image(image, width, height):
    width = int(width)
    height = int(height)
    aspect_ratio = image.width / image.height
    if height == 0:
        new_width = width
        new_height = int(round(width / aspect_ratio, 0))
    elif width == 0:
        new_height = height
        new_width = int(round(height * aspect_ratio, 0))
    else:
        new_width = width
        new_height = height

    image = image.resize((new_width, new_height))

    return image