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

#7.What is the percentage of placement in all branches without ESIGELEC in 2015

def percentage_all_ESIGELEC_2015():
	sample7=read.sheet1[read.sheet1.Year==2015]
	samp7=sample7[read.sheet1.MscTechProgram=='All branch without ESIGELEC']
	sam=samp7.Percentage
	print("percentage of placement in all branches without ESIGELEC in 2015 is:")
	print(sam)

if __name__=='__main__':
	percentage_all_ESIGELEC_2015()