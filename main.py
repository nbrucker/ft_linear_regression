import sys

import error

def isInt(x):
	try:
		int(x)
		return True
	except:
		return False

def getData(content):
	km = []
	price = []
	lines = content.split('\n')[1:]
	for line in lines:
		if (line == ''):
			continue
		data = line.split(',')
		if (len(data) != 2 or not isInt(data[0]) or not isInt(data[1])):
			error.error('Unexpected error')
		km.append(int(data[0]))
		price.append(int(data[1]))
	return ([km, price])

def test(data):
	m = len(data[0])
	i = 0
	theta0 = 0
	theta1 = 0
	while (i < m):
		estimated = theta0 + (theta1 * data[0][i])
		tmp0 = 1 * (1 / float(m)) * (estimated - data[1][i])
		tmp1 = 1 * (1 / float(m)) * ((estimated - data[1][i]) * data[0][i])
		theta0 = tmp0
		theta1 = tmp1
		i += 1
	print(theta0)
	print(theta1)

def main():
	if (len(sys.argv) != 2):
		error.error('python main.py [file]')
	filename = sys.argv[1]
	content = ''
	try:
		f = open(filename, 'r')
		content = f.read()
		f.close()
	except:
		error.error('error opening file')
	data = getData(content)
	test(data)

if __name__ == "__main__":
	main()
