# $ pip install qrcode

"""
import qrcode as qr

img = qr.make("https://github.com/Fakher-Zaman")
img.save("github_account.png")
"""

# pip install Pillow

import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1, error_correction=qrcode.ERROR_CORRECT_H, box_size=10, border=2)
qr.add_data("https://www.youtube.com/")
qr.make(fit=True)
img = qr.make_image(fill_color="blue", back_color="white")
img.save("google.png")