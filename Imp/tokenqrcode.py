 qr "https://www.fiverr.com/s/zLLjVd" token.png
 
 
 import qrcode

img = qrcode.make('Fiverr')
img.save('fiverr.png')

link = qrcode.make('https://www.fiverr.com/s/pLLraR')
link.save('token.png')

