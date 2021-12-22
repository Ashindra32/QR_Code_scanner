import qrcode
qr = qrcode.QRCode(version=1, box_size=50, border=4)
data = "https://www.google.com"
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="yellow")
img.save("qr1.png")
