#!/usr/bin/python3
""" This program can handle any number of price lists (operators) and then
calculate which operator is cheapest for a certain number."""

# Here we are using a regular expression (re) module which is a special sequence
# of characters that helps to match or find other strings or sets of strings.
import re

def make_dicts(file_input):
    """To make a dictionary with prefix as key and price as value"""
    with open(file_input) as file_1:
        price_list = {}
        for line in file_1:
            prefix, price = line.split()
			# Here we are spliting the phone numbers and prices from a file.
            price_list[prefix] = float(price)
    return price_list

def match_num(price_list, phone_num):
    """ Matching the phone number with the prefix from the price list"""
    out = {}
    for prefix in price_list:
        match_obj = re.match(prefix, phone_num, re.M|re.I)
        if match_obj:
            out = {}
            out[prefix] = price_list[prefix]
    return out

def operator_name(match_a, match_b):
    """ Calculating which operator is cheapest"""
    if not match_a:
        if not match_b:
            return "None"
        return "B"
    if not match_b:
        return "A"

    for key in match_a:
        final_a = match_a[key]

    for key in match_b:
        final_b = match_b[key]

    if final_a > final_b:
        final_op = "B"
    else:
        final_op = "A"

    return final_op

def main():
    """To determine the cheapest operator for the given number"""
    price_a = make_dicts("A_op.txt")
    price_b = make_dicts("B_op.txt")

    phone_num = input("Enter phone number: ")

    for k in phone_num:
        if k in ('+', '-'):
            phone_num = phone_num.replace(k, "")

    match_a = match_num(price_a, phone_num)
    print("match A: ", match_a)

    match_b = match_num(price_b, phone_num)
    print("match B: ", match_b)
    print("\n")

    final_op = operator_name(match_a, match_b)
    print("cheapest operator : ", final_op)

if __name__ == "__main__":
    main()
