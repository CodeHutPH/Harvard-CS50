import qrcode

img = qrcode.make("https://www.youtube.com/watch?v=EHi0RDZ31VA&ab_channel=CS50")
img.save("QRpy.png", "PNG")