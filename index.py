def main():
    # Choose number to convert
    num = input("Enter your number: ")
    
    # Choose what you're converting from
    number_type = int(input("Enter 1 to convert from decimal, 2 to convert from binary, 3 to convert from hex: "))
    
    if number_type == 1:
        decimalNum(num)
    elif number_type == 2:
        binaryNum(num)
    elif number_type == 3:
        hexNum(num)
    else:
        print("Please choose 1, 2, or 3")

def decimalNum(num):
    # Convert the input string to an integer
    num = int(num)
    
    # Convert decimal to binary
    bin = num
    binaryList = []
    while bin != 0:
        if bin % 2 == 0:
            binaryList.append(0)
        else:
            binaryList.append(1)
        bin = bin // 2   
    binaryList.reverse()
    binary_string = ''.join(map(str, binaryList))
    
    # Convert decimal to hex
    hex_num = num
    hexDigits = "0123456789ABCDEF"
    hexList = []
    while hex_num != 0:
        remainder = hex_num % 16
        hexList.append(hexDigits[remainder])
        hex_num = hex_num // 16
    hexList.reverse()
    hex_string = ''.join(hexList)
    
    # Print the results
    print(f"{num} in decimal is {binary_string} in binary and {hex_string} in hexadecimal")

def binaryNum(num):
    # Convert the input string to an integer with base 2
    decimal_num = int(num, 2)
    
    # Convert decimal to binary
    bin = decimal_num
    binaryList = []
    while bin != 0:
        if bin % 2 == 0:
            binaryList.append(0)
        else:
            binaryList.append(1)
        bin = bin // 2   
    binaryList.reverse()
    binary_string = ''.join(map(str, binaryList))
    
    # Convert decimal to hex
    hex_num = decimal_num
    hexDigits = "0123456789ABCDEF"
    hexList = []
    while hex_num != 0:
        remainder = hex_num % 16
        hexList.append(hexDigits[remainder])
        hex_num = hex_num // 16
    hexList.reverse()
    hex_string = ''.join(hexList)
    
    # Print the results
    print(f"{num} in binary is {decimal_num} in decimal and {hex_string} in hexadecimal")

def hexNum(num):
    # Convert the input string to an integer with base 16
    decimal_num = int(num, 16)
    
    # Convert decimal to binary
    bin = decimal_num
    binaryList = []
    while bin != 0:
        if bin % 2 == 0:
            binaryList.append(0)
        else:
            binaryList.append(1)
        bin = bin // 2   
    binaryList.reverse()
    binary_string = ''.join(map(str, binaryList))
    
    # Convert decimal to hex
    hex_num = decimal_num
    hexDigits = "0123456789ABCDEF"
    hexList = []
    while hex_num != 0:
        remainder = hex_num % 16
        hexList.append(hexDigits[remainder])
        hex_num = hex_num // 16
    hexList.reverse()
    hex_string = ''.join(hexList)
    
    # Print the results
    print(f"{num} in hexadecimal is {decimal_num} in decimal and {binary_string} in binary")

if __name__ == "__main__":
    main()
