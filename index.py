num



def main():
    num = input "enter your number":
    numberType = input "enter 1 to convert from decimal, 2 to convert from binary, 3 to convert from hex" :
            if numberType = 1:
                decimalNum(number)
            elif numberType = 2:
                binaryNum(number)
            elif numberType =3:
                hexNum(number)
            elif numberType = 4
                end
            else
                print ("please choose 1, 2, or 3")

def decimalNum():
num = int(input("number"))  
bin = num
binaryList = []
while bin != 0:
    if bin % 2 == 0:
        binaryList.append(0)
    else:
        binaryList.append(1)
    bin = bin // 2   

binaryList.reverse()
print(binaryList)

hex_num = num
hexDigits = "0123456789ABCDEF"
hexList = []

while hex_num != 0:
    remainder = hex_num % 16
    hexList.append(hexDigits[remainder])
    hex_num = hex_num // 16

hexList.reverse()
hex_string = ''.join(hexList)
print(hexList)

print(num + " in decimal is " + bin + " in binary " + " and " + hex_num " in hexadecimal")



def binaryNum():


def hexNum():