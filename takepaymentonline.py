import qrcode

#take UPI ID as a input 
upi_id = input("Enter your UPI ID =")

#upi://pay?pa=UPI_Id&pn=NAME&am=Amount%cu=CURRENCY&tn=MASSAGE

#Defining the payment URL based on the UPI ID and the payment app
#You can modify these URLs based on the payment apps 

phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#creat QR codes for each payment app

phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)


#Save the QR code to image file

phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')


#Display the QR code (you may need install PIL/Pillow Library)

phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()