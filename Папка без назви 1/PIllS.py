from PIL import Image
from PIL import ImageFilter

with Image.open('завантаження.jpg') as pic_original:
    pic_original.show()
    
    pic_gray = pic_original.convert('L')
    pic_gray.save('завантаження1.jpg')
    pic_gray.show()
    
    pic_up = pic_original.transpose(Image.ROTATE_90)
    pic_up.save('завантаження2.jpg')
    pic_up.show()