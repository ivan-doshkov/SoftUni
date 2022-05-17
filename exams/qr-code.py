import pyqrcode
import png
from pyqrcode import QRCode

adress = 'https://www.youtube.com/watch?v=E6V0IXyeqG4'
url = pyqrcode.create(adress)
url.png("London_view.png", scale=8)