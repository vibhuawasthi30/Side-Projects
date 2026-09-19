import qrcode

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=20,
                   border=2)

inputdata = input("Put Your Data In Here:")

qr.add_data(inputdata)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.name = input("What Will You Name You File:")
img.save(img.name + ".png")