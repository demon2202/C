def binary_to_decimal(binary_num):
    """Convert binary to decimal"""
    decimal_num = int(binary_num, 2)
    return decimal_num

def binary_to_octal(binary_num):
    """Convert binary to octal"""
    decimal_num = int(binary_num, 2)
    octal_num = oct(decimal_num).replace("0o", "")
    return octal_num

def binary_to_hexadecimal(binary_num):
    """Convert binary to hexadecimal"""
    decimal_num = int(binary_num, 2)
    hex_num = hex(decimal_num).replace("0x", "")
    return hex_num

def decimal_to_binary(decimal_num):
    """Convert decimal to binary"""
    binary_num = bin(decimal_num).replace("0b", "")
    return binary_num

def decimal_to_octal(decimal_num):
    """Convert decimal to octal"""
    octal_num = oct(decimal_num).replace("0o", "")
    return octal_num

def decimal_to_hexadecimal(decimal_num):
    """Convert decimal to hexadecimal"""
    hex_num = hex(decimal_num).replace("0x", "")
    return hex_num

def octal_to_binary(octal_num):
    """Convert octal to binary"""
    decimal_num = int(octal_num, 8)
    binary_num = bin(decimal_num).replace("0b", "")
    return binary_num

def octal_to_hexadecimal(octal_num):
    """Convert octal to hexadecimal"""
    decimal_num = int(octal_num, 8)
    hex_num = hex(decimal_num).replace("0x", "")
    return hex_num

def octal_to_decimal(octal_num):
    """Convert octal to decimal"""
    decimal_num = int(octal_num, 8)
    return decimal_num

def hexadecimal_to_binary(hex_num):
    """Convert hexadecimal to binary"""
    decimal_num = int(hex_num, 16)
    binary_num = bin(decimal_num).replace("0b", "")
    return binary_num

def hexadecimal_to_octal(hex_num):
    """Convert hexadecimal to octal"""
    decimal_num = int(hex_num, 16)
    octal_num = oct(decimal_num).replace("0o", "")
    return octal_num

def hexadecimal_to_decimal(hex_num):
    """Convert hexadecimal to decimal"""
    decimal_num = int(hex_num, 16)
    return decimal_num

# Example usage
binary_num = "1010"
decimal_num = binary_to_decimal(binary_num)
print(f"Binary {binary_num} to Decimal: {decimal_num}")

octal_num = "66"
decimal_num = octal_to_decimal(octal_num)
print(f"Octal {octal_num} to Decimal: {decimal_num}")

hex_num = "2F"
decimal_num = hexadecimal_to_decimal(hex_num)
print(f"Hexadecimal {hex_num} to Decimal: {decimal_num}")
