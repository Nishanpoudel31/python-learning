
import qrcode
qr_text = "Nishan Poudel$"
img = qrcode.make(qr_text)
type(img)  
img.save("nishan.png")
print("Qr code generated sucessfully")