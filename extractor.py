import csv
import numpy as np
import matplotlib.pyplot as plt
import logging



# Class to extract data
class extractor():
	def __init__(self,file):
		self.count=0
		self.file=file
		self.a={}

	def extraer(self):
		d={}
		f = open(self.file,"rb")
		reader = csv.reader(f)
		headers=reader.next()
		# print headers
		for i in headers:
			d[i]=[]
		for row in reader:
			for h,v in zip(headers,row):
				d[h].append(float(v))

		self.a=d		
	def test(self):
		print self.a

# Script Top
ext = extractor("conteo.csv")
ext.extraer()
ext.test()
