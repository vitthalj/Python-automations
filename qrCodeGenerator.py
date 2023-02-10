import qrcode
#data to be encode in QR code
data = input('Please enter data to be encoded: ')
qr = qrcode.QRCode(
    version = 1,
    box_size = 10,
    border = 5)

qr.add_data(data)
qr.make(fit = True)

image = qr.make_image(fill_color = 'red',back_color='white')
print('QR code is generated!!')
image.save('gitcolorQRcode.png')
