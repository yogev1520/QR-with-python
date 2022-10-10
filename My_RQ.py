import qrcode

website_link = 'https://www.youtube.com/watch?v=qz52QmuTL6A&list=PLmPuLIibbKEWv_Sdntn2srX474afILxbu'

qr = qrcode.QRCode(version = 1, box_size = 2, border = 2)

qr.add_data(website_link)
qr.make()

img = qr.make_image(fill_color = 'black', back_color = 'white')

img.save('youtube_qr.png')