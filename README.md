# QR-with-python
QR with python sorce artical = https://dev.to/codedex/generate-a-qr-code-with-python-386m

sorce git = https://github.com/lincolnloop/python-qrcode

lib requiers  = pip install qrcode pillow

import qrcode

Creating the QR Code
First, we want a link that we want to showcase. Let's use a classic YouTube video.

website_link = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

Next, we want to create an instance of qrcode. Since it's a Python library, we can call the package constructor to create a qrcode object, customized to our specifications.

In this example, we will create a QR code with a version of 1, and a box size and border size of 5.

qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)

The version parameter is an integer from 1 to 40 that controls the size of the QR code.
The box_size parameter controls how many pixels each “box” of the QR code is.
The border parameter controls how many boxes thick the border should be.
As an exercise, try taking in these parameters as input, and explaining to the user how to set this up, so they can create the QR code to their own specifications.

Visit documentation for more information about the parameters in qrcode.QRCode(...)https://github.com/lincolnloop/python-qrcode 


sorce project = https://dev.to/codedex/generate-a-qr-code-with-python-386m
