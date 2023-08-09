import qrcode

qr = qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                  box_size=10, border=4)
qr.add_data("<Your URL>")
qr.make(fit=True)
img = qr.make_image(fill_color="orange", back_color="white")
img.save("pravesh.png")
