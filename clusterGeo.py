import pandas as pd
import csv
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

def loadCSV (csvName) :
	rawData = pd.read_csv(csvName, sep = ',')
	return rawData

def pairs(rawData) :
	lati = list(rawData['0'])
	longi = list(rawData['1'])
	return np.array(zip(lati, longi))

def kMeans (data, numK):
	random_state = 170
	kmeans = KMeans(n_clusters = numK, random_state=random_state).fit(data)
	return kmeans


if __name__ == '__main__' :
	csvPath = 'coord.csv'
	rawData = loadCSV(csvPath)
	numClust = 8
	#print list(data['0'])
	data = pairs(rawData)
	kmeansRes = kMeans(data, numClust)
	plt.figure(figsize=(12, 12))
	y_ = kmeansRes.labels_
	#print y_
	xmin = -124.848974
	xmax = 24.396308
	ymin = -66.885444
	ymax = 49.384358
	axes = plt.gca()
	axes.set_xlim([xmin,xmax])
	axes.set_ylim([ymin,ymax])
	plt.scatter(data[:, 1], data[:, 0], c = y_)
	plt.show()
