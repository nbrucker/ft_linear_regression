import sys
import json

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

def checkData(thetas, key, f):
	if (key not in thetas or not f(thetas[key])):
		thetas[key] = 0
	return thetas

def main():
	if (len(sys.argv) != 1):
		error.error('python predict.py')
	x = input('Mileage ? ')
	if (not isInt(x)):
		error.error('Invalid mileage')
	x = int(x)
	content = ''
	thetas = {}
	try:
		f = open('thetas.json', 'r')
		content = f.read()
		f.close()
		thetas = json.loads(content)
	except:
		error.error('0')
	thetas = checkData(thetas, 'theta0', isFloat)
	thetas = checkData(thetas, 'theta1', isFloat)
	thetas = checkData(thetas, 'min', isInt)
	thetas = checkData(thetas, 'max', isInt)
	div = float(int(thetas['max']) - int(thetas['min']))
	if (div == 0):
		div = float(1)
	x = (x - int(thetas['min'])) / div
	print(hypothesis.hypothesis(float(thetas['theta0']), float(thetas['theta1']), x))

if __name__ == "__main__":
	main()
