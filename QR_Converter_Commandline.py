# Simple app to create QR codes

import qrcode

def generate_qrcode(text):
    suffix = '.png'
    filename = 'QR'

    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 20,
        border = 5,        
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill="black", backcolor="white")
    # img.save("QR_Save.png")
    img.save(f'{filename} _ {text} {suffix}') #(f'{guy} is dating {girl}')


url = input("Enter your url:")
generate_qrcode(url)