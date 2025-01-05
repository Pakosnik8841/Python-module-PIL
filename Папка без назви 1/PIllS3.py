from PIL import Image
from PIL import ImageFilter

with Image.open('завантаження.jpg') as pic_original:
    
    pic_blured = pic_original.filter(ImageFilter.BLUR)
    pic_blured.save('завантаження4.jpg')
    pic_blured.show()