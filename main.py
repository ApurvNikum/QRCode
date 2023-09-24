import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import RadialGradiantColorMask

import os

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4,
)
qr.add_data(os.environ['LINK'])
qr.make(fit=True)

img = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask())
# img = qr.make_image(fill_color="black", back_color="white")

img.save('qr_code.png')
