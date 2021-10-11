import qrcode
img = qrcode.make('Some data here')
type(img)  # qrcode.image.pil.PilImage
img.save("/home/geek/Desktop/PythonOthers/some_file.png")
