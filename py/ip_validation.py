# Write an algorithm that will identify valid IPv4 addresses in dot-decimal format.
# IPs should be considered valid if they consist of four octets, with values between
# 0 and 255, inclusive.

# Valid inputs examples:
# Examples of valid inputs:
# 1.2.3.4
# 123.45.67.89
# Invalid input examples:
# 1.2.3
# 1.2.3.4.5
# 123.456.78.90
# 123.045.067.089
# Notes:
# Leading zeros (e.g. 01.02.03.04) are considered invalid
# Inputs are guaranteed to be a single string

# PROBLEM
# ----------------
#
# INPUT: String
# OUTPUT: Boolean (format of IP adresss is valid?)
#
# RULES:
# - Leading zeros are considered invalid
# - Inputs will be only single string
# - 4 numbers from 1 to 255 separated by 3 dots
#
# EXAMPLES
# ----------------
#
# INPUT: 1.2.3.4
# => 1
# =>
# OUTPUT: True
#
# DATA STRUCTURES
# ----------------
#
# INPUT:
# =>
# OUTPUT:
#
# ALGORITHM
# ----------------
#
#
# NOTES:
#
# WHAT:
#
# HOW:
#

def is_valid_IP(strng):
    strng.split(".")

print('Test result is ' + str(is_valid_IP('12.255.56.1') ==     True))
print(is_valid_IP('12.255.56.1')) #     True

print('Test result is ' + str(is_valid_IP('') ==                False))
print(is_valid_IP('')) #                False

print('Test result is ' + str(is_valid_IP('abc.def.ghi.jkl') == False))
print(is_valid_IP('abc.def.ghi.jkl')) # False

print('Test result is ' + str(is_valid_IP('123.456.789.0') ==   False))
print(is_valid_IP('123.456.789.0')) #   False

print('Test result is ' + str(is_valid_IP('12.34.56') ==        False))
print(is_valid_IP('12.34.56')) #        False

print('Test result is ' + str(is_valid_IP('12.34.56 .1') ==     False))
print(is_valid_IP('12.34.56 .1')) #     False

print('Test result is ' + str(is_valid_IP('12.34.56.-1') ==     False))
print(is_valid_IP('12.34.56.-1')) #     False

print('Test result is ' + str(is_valid_IP('123.045.067.089') == False))
print(is_valid_IP('123.045.067.089')) # False

print('Test result is ' + str(is_valid_IP('127.1.1.0') ==        True))
print(is_valid_IP('127.1.1.0')) #        True

print('Test result is ' + str(is_valid_IP('0.0.0.0') ==          True))
print(is_valid_IP('0.0.0.0')) #          True

print('Test result is ' + str(is_valid_IP('0.34.82.53') ==       True))
print(is_valid_IP('0.34.82.53')) #       True

print('Test result is ' + str(is_valid_IP('192.168.1.300') ==   False))
print(is_valid_IP('192.168.1.300')) #   False