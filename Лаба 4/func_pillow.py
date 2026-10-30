from PIL import Image
def create_blank_image(filename="blank.png"):
    Image.new("RGB", (100, 100), color="red").save(filename)
    return f"Зображення створено: {filename}"
