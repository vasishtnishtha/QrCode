import qrcode as qr

img = qr.make(
    "https://www.youtube.com/watch?v=FOGRHBp6lvM&list=PLjVLYmrlmjGfAUdLiF2bQ-0l8SwNZ1sBl&ab_channel=WsCubeTech")
img.save("youtube_qr.png")
