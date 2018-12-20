import sys

import error
import hypothesis

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
		km.append(int(data[0]) / float(10000))
		price.append(int(data[1]))
	data = {}
	data['km'] = km
	data['price'] = price
	return (data)

def train(data):
	m = len(data['km'])
	i = 1
	theta0 = 0
	theta1 = 0
	while (i < 2000):
		j = 0
		tmp0 = 0
		tmp1 = 0
		while (j < m):
			estimated = hypothesis.hypothesis(theta0, theta1, data['km'][j])
			tmp0 = estimated - data['price'][j]
			tmp1 = (estimated - data['price'][j]) * data['km'][j]
			j += 1
		theta0 -= (1 / float(i)) * (1 / float(m)) * tmp0
		theta1 -= (1 / float(i)) * (1 / float(m)) * tmp1
		i += 1
	return theta0, theta1

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
	t0, t1 = train(data)
	print(t0)
	print(t1)

if __name__ == "__main__":
	main()
