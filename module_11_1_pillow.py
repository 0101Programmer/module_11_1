import requests
from PIL import Image, ImageDraw

filename = "some_pillow.jpg"

# Просмотр изображения
# with Image.open(filename) as img:
#     img.show()


# Обрезка изображения и сохранение в другом формате
# image = Image.open('some_pillow.jpg')
# cropped = image.crop((10, 100, 400, 500))
# cropped.save(r'C:\Users\vavan\PythonProjectsUrban\bibl\cropped_pillow.png')

# Поворот изображения и сохранение в другом формате
# image = Image.open('some_pillow.jpg')
# rotated = image.rotate(180)
# rotated.save('image_rotated.jpg')

# сохранение изображения из интернета
# URL = ('https://get.pxhere.com/photo/leaf-flower-petal-home-green-umbrella-clean-rest-furniture-pillow-material'
#        '-cushion-textile-art-sleep-design-bed-comfort-domestic-cotton-household-pillows-bedding-bed-sheet-pile-of'
#        '-pillows-902708.jpg')
# open_url = requests.get(URL, stream=True).raw
# image = Image.open(open_url)
# image.save('pillow_tower.jpg', 'jpeg')

# создание нового изображения (зелёный прямоугольник)
# new = Image.new(mode="RGBA", size=(400, 200), color='green')
# new.show()
