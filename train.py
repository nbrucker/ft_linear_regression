import sys
import matplotlib.pyplot as plt
import json

import error
import hypothesis

def isInt(x):
	try:
		int(x)
		return True
	except:
		return False

def getData(content):
	min = None
	max = None
	km = []
	price = []
	lines = content.split('\n')[1:]
	for line in lines:
		if (line == ''):
			continue
		data = line.split(',')
		if (len(data) != 2 or not isInt(data[0]) or not isInt(data[1])):
			error.error('Unexpected error')
		if (min is None or int(data[0]) < min):
			min = int(data[0])
		if (max is None or int(data[0]) > max):
			max = int(data[0])
		km.append(int(data[0]))
		price.append(int(data[1]))
	data = {}
	data['km'] = km
	data['price'] = price
	return (data, min, max)

def train(data):
	m = len(data['km'])
	i = 1
	theta0 = 0
	theta1 = 0
	old_cost = None
	cost = None
	while (old_cost is None or round(old_cost, 2) != round(cost, 2)):
		j = 0
		tmp0 = 0
		tmp1 = 0
		old_cost = cost
		cost = 0
		while (j < m):
			estimated = hypothesis.hypothesis(theta0, theta1, data['km'][j])
			cost += pow(estimated - data['price'][j], 2)
			tmp0 += estimated - data['price'][j]
			tmp1 += (estimated - data['price'][j]) * data['km'][j]
			j += 1
		cost *= (1 / float(2 * m))
		theta0 -= (1 / float(i)) * (1 / float(m)) * tmp0
		theta1 -= (1 / float(i)) * (1 / float(m)) * tmp1
		i += 1
	return theta0, theta1

def scale(data, min, max):
	i = 0
	div = float(max - min)
	if (div == 0):
		div = float(1)
	while (i < len(data['km'])):
		data['km'][i] = (data['km'][i] - min) / div
		i += 1
	return data

def saveTheta(t0, t1, min, max):
	output = {
		'theta0': t0,
		'theta1': t1,
		'min': min,
		'max': max
	}
	open('thetas.json', 'w').close()
	f = open('thetas.json', 'w')
	f.write(json.dumps(output))
	f.close()

def main():
	if (len(sys.argv) != 2):
		error.error('python train.py [file]')
	filename = sys.argv[1]
	content = ''
	try:
		f = open(filename, 'r')
		content = f.read()
		f.close()
	except:
		error.error('error opening file')
	data, min, max = getData(content)
	if (len(data) < 1):
		error.error('no data')
	data = scale(data, min, max)
	t0, t1 = train(data)
	saveTheta(t0, t1, min, max)
	i = 0
	predict = []
	while (i < len(data['km'])):
		predict.append(hypothesis.hypothesis(t0, t1, data['km'][i]))
		i += 1
	plt.scatter(data['km'], data['price'], color='blue')
	plt.plot(data['km'], predict, color='red', linewidth=2)
	plt.xticks([])
	plt.yticks([])
	plt.show()

if __name__ == "__main__":
	main()
