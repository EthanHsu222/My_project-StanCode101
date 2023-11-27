"""
File: coin_flip_runs.py
Name:Ethan HSU
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
	"""
	TODO:Randomly flip H or T and count how many has it been
	"""
	print("Let's flip a coin!")
	numtorun = int(input('Number of runs: '))
	count = 0
	in_a_row = False
	num = r.randint(1, 2)
	if num == 1:
		print('H', end='')
	else:
		print('T', end='')
	while True:
		if count != numtorun:
			num2 = r.randint(1, 2)
			if num2 == 1:
				print('H', end='')
			else:
				print('T', end='')
			if num == num2:
				if not in_a_row:
					count += 1
					in_a_row = True
			else:
				in_a_row = False
			num2 = num2
		else:
			break


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
