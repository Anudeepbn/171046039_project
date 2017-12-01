import read
'''import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

import sys

#### read excel sheet

sheet1= pd.read_excel('Placementsois.xlsx',sheetname='placementstats')


sheet2=pd.read_excel('Placementsois.xlsx',sheetname='enrollment')


sheet1_reindexing=sheet1.reset_index()
'''
#sheet2=sheet2.drop(sheet2.index[])
##Analysis

#5.How many number of students are ESIGELEC in the year 2014


def ESIGELEC_2014():
	sample5=read.sheet2[read.sheet2.Year==2014]
	sam5=sample5[read.sheet2.Company=='ESIGELEC']
	print("Number of students are ESIGELEC in the year 2014")
	print(sam5.Company.count())

if __name__=='__main__':
	ESIGELEC_2014()