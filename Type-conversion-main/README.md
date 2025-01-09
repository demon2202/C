# Type Conversion
This repository covers various type conversion operations with detailed explanations and examples for each conversion type

## Introduction

Welcome to the comprehensive guide on converting between binary, decimal, octal, and hexadecimal numbers. Understanding how to convert between these number systems is essential for various applications in computer science, digital electronics, and programming.

## Table of Contents

1. [Binary to Decimal Conversion](#binary-to-decimal-conversion)
2. [Binary to Octal Conversion](#binary-to-octal-conversion)
3. [Binary to Hexadecimal Conversion](#binary-to-hexadecimal-conversion)
4. [Decimal to Binary Conversion](#decimal-to-binary-conversion)
5. [Decimal to Octal Conversion](#decimal-to-octal-conversion)
6. [Decimal to Hexadecimal Conversion](#decimal-to-hexadecimal-conversion)
7. [Octal to Binary Conversion](#octal-to-binary-conversion)
8. [Octal to Hexadecimal Conversion](#octal-to-hexadecimal-conversion)
9. [Octal to Decimal Conversion](#octal-to-decimal-conversion)
10. [Hexadecimal to Binary Conversion](#hexadecimal-to-binary-conversion)
11. [Hexadecimal to Decimal Conversion](#hexadecimal-to-decimal-conversion)
12. [Hexadecimal to Octal Conversion](#hexadecimal-to-octal-conversion)

## Binary to Decimal Conversion

### Procedure:

1. Write down the binary number.
2. Starting from the rightmost digit, assign powers of 2 to each digit from right to left, starting from 2^0 for the rightmost digit.
3. Multiply each binary digit by its corresponding power of 2.
4. Sum up all the products to get the decimal equivalent.

### Example:

Binary Number: 1010

Procedure:

```
(1 * 2^3) + (0 * 2^2) + (1 * 2^1) + (0 * 2^0)
= (1 * 8) + (0 * 4) + (1 * 2) + (0 * 1)
= 8 + 0 + 2 + 0
= 10 (Decimal Equivalent)
```

## Binary to Octal Conversion

### Procedure:

1. Group the binary digits into sets of three, starting from the right.
2. If necessary, add leading zeros to the leftmost group to make it a complete set of three.
3. Convert each group of three binary digits to its octal equivalent.

### Example:

Binary Number: 110110

Procedure:

```
(011) (011) (0)
3     3     0
```

Octal Equivalent: 66

## Binary to Hexadecimal Conversion

### Procedure:

1. Group the binary digits into sets of four, starting from the right.
2. If necessary, add leading zeros to the leftmost group to make it a complete set of four.
3. Convert each group of four binary digits to its hexadecimal equivalent.

### Example:

Binary Number: 11011011

Procedure:

```
(1101) (1011)
D       B
```

Hexadecimal Equivalent: DB

## Decimal to Binary Conversion

### Procedure:

1. Divide the decimal number by 2.
2. Keep track of the remainders obtained at each division (0 or 1).
3. Continue dividing until the quotient is 0.
4. Write the remainders in reverse order to obtain the binary equivalent.

### Example:

Decimal Number: 15

Procedure:

```
15 ÷ 2 = 7 remainder 1
7 ÷ 2 = 3 remainder 1
3 ÷ 2 = 1 remainder 1
1 ÷ 2 = 0 remainder 1
```

Binary Equivalent: 1111

## Decimal to Octal Conversion

### Procedure:

1. Divide the decimal number by 8.
2. Keep track of the remainders obtained at each division.
3. Write the remainders in reverse order to obtain the octal equivalent.

### Example:

Decimal Number: 45

Procedure:

```
45 ÷ 8 = 5 remainder 5
5 ÷ 8 = 0 remainder 5
```

Octal Equivalent: 55

## Decimal to Hexadecimal Conversion

### Procedure:

1. Divide the decimal number by 16.
2. Keep track of the remainders obtained at each division.
3. Convert remainders greater than 9 to their corresponding hexadecimal letters (A, B, C, D, E, F).
4. Write the remainders in reverse order to obtain the hexadecimal equivalent.

### Example:

Decimal Number: 123

Procedure:

```
123 ÷ 16 = 7 remainder 11 (B)
7 ÷ 16 = 0 remainder 7
```

Hexadecimal Equivalent: 7B

## Octal to Binary Conversion

### Procedure:

1. Convert each octal digit to its binary equivalent.
2. Combine the binary equivalents of all the octal digits.

### Example:

Octal Number: 75

Procedure:

```
7 -> 111, 5 ->

 101
```

Binary Equivalent: 111101

## Octal to Hexadecimal Conversion

### Procedure:

1. Convert the octal number to binary.
2. Convert the binary number to hexadecimal.

## Octal to Decimal Conversion

### Procedure:

1. Write down the octal number.
2. Assign powers of 8 to each digit from right to left, starting from 8^0 for the rightmost digit.
3. Multiply each octal digit by its corresponding power of 8.
4. Sum up all the products to get the decimal equivalent.

### Example:

Octal Number: 66

Procedure:

```
(6 * 8^1) + (6 * 8^0)
= (6 * 8) + (6 * 1)
= 48 + 6
= 54 (Decimal Equivalent)
```

## Hexadecimal to Binary Conversion

### Procedure:

1. Convert each hexadecimal digit to its binary equivalent.
2. Combine the binary equivalents of all the hexadecimal digits.

### Example:

Hexadecimal Number: 1A3

Procedure:

```
1 -> 0001, A -> 1010, 3 -> 0011
```

Binary Equivalent: 000110100011

## Hexadecimal to Decimal Conversion

### Procedure:

1. Write down the hexadecimal number.
2. Assign powers of 16 to each digit from right to left, starting from 16^0 for the rightmost digit.
3. Multiply each hexadecimal digit by its corresponding power of 16.
4. Sum up all the products to get the decimal equivalent.

### Example:

Hexadecimal Number: 2F

Procedure:

```
(2 * 16^1) + (F * 16^0)
= (2 * 16) + (15 * 1)
= 32 + 15
= 47 (Decimal Equivalent)
```

## Hexadecimal to Octal Conversion

### Procedure:

1. Convert the hexadecimal number to binary.
2. Convert the binary number to octal.

## Conclusion

Mastering the conversion between binary, decimal, octal, and hexadecimal numbers is fundamental in various fields, including computer science and digital electronics. By understanding these conversions, you can work more effectively with different number systems and solve a wide range of problems. We hope this guide has provided you with a comprehensive understanding of these conversions. Happy learning and coding!

--- 

Feel free to customize this README file according to your preferences and needs. Let me know if you need further assistance!
