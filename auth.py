import random

otp_storage = {}

def generate_otp(email):

    otp = random.randint(100000,999999)

    otp_storage[email] = otp

    print(f"OTP for {email} is {otp}")  # simulate email

    return "OTP sent to email"


def verify_otp(email, otp):

    if email in otp_storage and otp_storage[email] == int(otp):
        return True

    return False