  CSC221 Project 2 Design Document
By nate, dylan, and danica
Solution: 

-The software is written in pseudocode, converting binary, decimal, and hexadecimal
to one another.


Overview of software:

-The software will run as a Binary-Hex-Dec converter.
-The software will address the problem of converting binary, decimal, and hexadecimal
all to one another.


Analysis of Software:

-The software will run as a binary-hexadecimal converter.
-The software needs to take the input and convert to either hexadecimal, decimal, or binary. 


Algorithm to be used in Software:

#This one selects the number then selects the base number system. 
Def Main
Take input to convert
Select a number
If 1,
call decimal  ()
Else if 2,
call binary ()
Else if 3,
call Hex ()
Else if 4,
	end ()
Else, 
try again, call main ()
	



#If they select decimal, then this converts the number from decimal to binary and hexadecimal, and then prints them out.
Def Decimal
Convert to binary
Convert to hex
Print “number” is “hexnumber” in hex and “binarynumber” in binary
Call main

#If they select binary, then this converts the number from binary to decimal and hexadecimal, and then prints them out.
Def Binary
Convert to decimal
Convert to hex
Print “number” is “hexnumber” in hex and “decimalnumber” in decimal
Call main

#If they select hexadecimal, then this converts the number from hexadecimal to binary and decimal, and then prints them out.
Def Hex
Convert to binary
Convert to Decimal
Print “number” is “decimalnumber” in decimal and “binarynumber” in binary
Call main
-Top-Down















Pseudo Code For Converter 			


MAIN FUNCTION:
    PROMPT user to enter a number and STORE it in 'num'
    PROMPT user to choose a conversion type:
        1 for decimal to binary and hex
        2 for binary to decimal and hex
        3 for hex to decimal and binary
    STORE the choice in 'number_type'
    
    IF 'number_type' is 1:
        CALL decimalNum with 'num'
    ELSE IF 'number_type' is 2:
        CALL binaryNum with 'num'
    ELSE IF 'number_type' is 3:
        CALL hexNum with 'num'
    ELSE:
        PRINT "Please choose 1, 2, or 3"


DECIMALNUM FUNCTION:
    CONVERT 'num' from string to integer
    CONVERT integer to binary:
        INITIALIZE an empty list 'binaryList'
        WHILE integer is not 0:
            APPEND 0 to 'binaryList' if integer is even
            APPEND 1 to 'binaryList' if integer is odd
            DIVIDE integer by 2
        REVERSE 'binaryList'
        JOIN 'binaryList' to form 'binary_string'
    
    CONVERT integer to hexadecimal:
        INITIALIZE an empty list 'hexList'
        DEFINE 'hexDigits' as "0123456789ABCDEF"
        WHILE integer is not 0:
            COMPUTE remainder of integer divided by 16
            APPEND corresponding hex digit to 'hexList'
            DIVIDE integer by 16
        REVERSE 'hexList'
        JOIN 'hexList' to form 'hex_string'
    
    PRINT the results of conversion


BINARYNUM FUNCTION:
    CONVERT 'num' from binary string to integer
    CONVERT integer to binary (same steps as in decimalNum)
    CONVERT integer to hexadecimal (same steps as in decimalNum)
    PRINT the results of conversion


HEXNUM FUNCTION:
    CONVERT 'num' from hex string to integer
    CONVERT integer to binary (same steps as in decimalNum)
    CONVERT integer to hexadecimal (same steps as in decimalNum)
    PRINT the results of conversion


IF this script is the main program:
    CALL main function
