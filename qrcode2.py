import qrcode

img_url = input('INPUT URL FOR QR CODE: ')
savefilename = input('INPUT SAVEFILENAME: ')
                      
qr_gen = qrcode.make(img_url)
qr_gen.save(savefilename)

print(qr_gen) 
print(qr_gen.size)

