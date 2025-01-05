from PIL import Image

with Image.open('завантаження.jpg') as pic_original:
    print('Розмір:', pic_original.size)
    print('Формат:', pic_original.format)
    print('Тип:', pic_original.mode)
    pic_original.show()