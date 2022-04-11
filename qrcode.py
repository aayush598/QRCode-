# qrcode generator
import pyqrcode
# import png
def qrcode():
    qr_text=input('Enter the text: ')
    qr=pyqrcode.create(qr_text)
    qr.svg('myqr.svg',scale=8)
qrcode()
