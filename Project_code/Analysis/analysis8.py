import read
'''import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

import sys

#### read excel sheet

sheet1= pd.read_excel('Placementsois.xlsx',sheetname='placementstats')


sheet2= pd.read_excel('Placementsois.xlsx',sheetname='enrollment')


sheet1_reindexing=sheet1.reset_index()
'''
#sheet2=sheet2.drop(sheet2.index[])
##Analysis

#8.Display all companies that are attending SOIS department
def all_companies():
	sample8=read.sheet2[read.sheet2.Year==2012]#,sheet2.Year==2013,sheet2.Year==2014,sheet2.Year==2015,sheet2.Year==2016]
	samp8=sample8.Company.unique()
	#print(samp8)
	#print(len(samp8))
	#value = None
	#while value in samp8:
    #samp8.remove(value)
	
	s=[]
	for i in samp8:
		if i not in s:
			s.append(i)
	for i in s:
		print(i)

	#a=np.unique(samp8).tolist()
	#print(i.count())

if __name__=='__main__':
	all_companies()