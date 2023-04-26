import image
import qrcode
qr = qrcode.QRCode(
    version=5,#complexity in qr design
    box_size=10,
    border = 5 
)
data="https://app.lofi.co/" #path of qr to generate
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="white",white_color="black")
img.save("test.png")
 