#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_bill(name, data):
	INDEX_NAME = 0
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2
	sous_total = 0
	for tuple in data:
		sous_total += tuple[1]*tuple[2]
	taxes = 0.15*sous_total
	total = sous_total + taxes

	return (f"{name}\n"
			f"SOUS TOTAL     {sous_total:.2f} $\n"
			f"TAXES           {taxes:.2f} $\n"
			f"TOTAL          {total:.2f} $")


def format_number(number, num_decimal_digits):
	if number > 0:
		decimals = str(number).find('.')
		intermediary = str(int(number))
		start = -1
		result = ''
		for i in range(2,len(intermediary), 3):
			result += intermediary[start:(-i-2):-1] + ' '
			start -= 3
		result += intermediary[start::-1]
		return (result[::-1] + '.' + str(number)[decimals + 1:decimals +1+num_decimal_digits]).lstrip()
	else:
		number = -number
		decimals = str(number).find('.')
		intermediary = str(int(number))
		start = -1
		result = ''
		for i in range(2, len(intermediary), 3):
			result += intermediary[start:(-i - 2):-1] + ' '
			start -= 3
		result += intermediary[start::-1]
		return '-' + (result[::-1] + '.' + str(number)[decimals + 1:decimals + 1 + num_decimal_digits]).lstrip()

def get_triangle(num_rows):
	shape = ('+'*(num_rows*2 + 1))+'\n'
	nb_a = 'A'
	spacing = ' '*(num_rows - 1)
	for i in range(num_rows):
		shape += '+' + spacing + nb_a + spacing + '+'+'\n'
		spacing = ' '*(len(spacing)-1)
		nb_a += 'AA'
	shape += '+'*(num_rows*2 + 1) + '\n'
	return shape



if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

	print(format_number(-12345.678, 2))

	print(get_triangle(2))
	print(get_triangle(5))
