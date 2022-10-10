import qrcode

website_link = 'https://github.com/yogev1520'

qr = qrcode.QRCode(version = 1, box_size = 2, border = 2)

qr.add_data(website_link)
qr.make()

img = qr.make_image(fill_color = 'yellow', back_color = 'blue')

img.save('youtube_qr.png')