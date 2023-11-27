"""
File: class_reviews.py
Name:ethan HSU
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101)
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""
"""
classes = input class
classes1 all upper 
diff classes type 
score001 , score101 

"""
EXIT = "-1"


def main():
	classes = str(input('Which Class?: '))
	classes = classes.upper()
	#101 & 001
	times101 = 0
	times001 = 0
	data101 = 0
	data001 = 0
	max101 = 0
	max001 = 0
	min101 = 0
	min001 = 0
	if classes != str(EXIT):
		data = int(input('Score : '))
		if classes == "SC101":
			max_score101 = data
			min_score101 = data
			times101 = 1

		elif classes == "SC001":
			max_score001 = data
			min_score001 = data
			times001 = 1
		avg_101 = 0
		avg_001 = 0
		while True:
			if classes != str(EXIT):
				if classes == 'SC101':
					if times101 == 0:
						max_score101 = data
						min_score101 = data
						times101 = 1
						data101 = data
					else:
						data += data
						times101 += 1
						avg101 = data101/times101
						if data > max101:
							max101 = data
						if data < min101:
							min101 = data
				elif classes == str("SC001"):
					if times001 == 0:
						max001 = data
						min001 = data
						times001 = 1
						data001 = data
					else :
						data001 +=data
						times001 += 1
						avg001 = data001 / times001
						if data > max001:
							maximum_101 = data
						elif data < min001:
							minimum_101 = data
			classes = str(input('Which class ?: '))
			classes = classes.upper()

			if classes == str(EXIT):
				print("==========SC001==========")
				if times001 != 0:
					print('Max = ' + str(max001))
					print('min = ' + str(min001))
					print('Average = ' + str(avg001))
				else:
					print("NoScore for 001")
				print("==========SC101==========")
				if times101 != 0:
					print('Max = ' + str(max101))
					print('min = ' + str(min101))
					print('Average = ' + str(avg101))
				else:
					print("No score for 101")
				break
			data = int(input('Score : '))
		else:
			print("No class scores were entered !")



# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
	main()
