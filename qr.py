import qrcode

link = input("Please provide link: ")
img = qrcode.make(link)
img.save("qr.png", "PNG")
