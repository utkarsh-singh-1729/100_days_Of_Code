import math, random
def generateOTP():
    
    digits = "0123456789"
    OTP = ""

    
    for i in range(6):
        OTP += digits[math.floor(random.random() * 10)]

    return OTP



if __name__ == "__main__":
    print("OTP of 6 digits:", generateOTP())
