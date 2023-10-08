import smtplib
import random
import getpass
import sys

def send_otp(email):
    otp = ''.join([str(random.randint(0, 9)) for i in range(6)])
    message = 'Subject: {}\n\n{}'.format('OTP for verification', 'Your OTP is: ' + otp)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('your_email@gmail.com', 'your_password')
        server.sendmail('your_email@gmail.com', email, message)
        server.quit()
        print("OTP sent successfully.")
    except Exception as e:
        print("Error occurred: ", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python send_otp.py <user_email>")
        sys.exit(1)
    
    email = sys.argv[1]
    send_otp(email)
