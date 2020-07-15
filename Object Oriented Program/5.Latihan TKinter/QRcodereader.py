# before please install this:
# pip install pillow
# pip install pyzbar

from pyzbar.pyzbar import decode
from PIL import Image
d=decode(Image.open('C:\\test.jpg'))
print(d[0].data.decode())

# image = Image.open('C:\\test.jpg')
# image.show()