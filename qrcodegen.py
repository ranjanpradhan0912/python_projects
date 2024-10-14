import qrcode

# function that takes user input
def input_user():
    text = input("Enter the text or url: ")
    file_name = input("Enter the file name: ")
    return text,file_name

#function that generates qrcode
def qrcode_generator(text,file):
 qr=qrcode.QRCode(
     version=1,
     error_correction=qrcode.constants.ERROR_CORRECT_H,
     box_size=10,
     border=4
 )
 qr.add_data(text)
 qr.make(fit=True)

 img=qr.make_image(fill_color='#091235',back_color='#88a9c3')

 img.save(f'{file}.png',format='png')

user_details=input_user()
qrcode_generator(user_details[0],user_details[1])