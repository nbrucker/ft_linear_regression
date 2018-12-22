import sys

import error
import hypothesis

def isFloat(x):
	try:
		float(x)
		return True
	except:
		return False

def isInt(x):
	try:
		int(x)
		return True
	except:
		return False

def main():
	if (len(sys.argv) != 2):
		error.error('python predict.py [x]')
	x = sys.argv[1]
	if (not isInt(x)):
		error.error('Invalid parameter')
	x = int(x)
	content = ''
	try:
		f = open('theta', 'r')
		content = f.read()
		f.close()
	except:
		error.error('error opening file')
	theta = content.split(',')
	if (len(theta) != 2 or not isFloat(theta[0]) or not isFloat(theta[1])):
		error.error('Unexpected error')
	theta[0] = float(theta[0])
	theta[1] = float(theta[1])
	print(hypothesis.hypothesis(theta[0], theta[1], x))

if __name__ == "__main__":
	main()
