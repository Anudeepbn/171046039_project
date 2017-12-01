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



#4.List out all the students B.E aggregrate  who hired by  iSoft Mangalore in 2012 batch

def iSoft_BE_Aggregrate():
	sample4=read.sheet2[read.sheet2.Year==2012]
	samp4=sample4[read.sheet2.Company=='iSoft, Mangalore']
	sam4=samp4.BE_Aggregate
	print(sam4)

if __name__=='__main__':
	iSoft_BE_Aggregrate()