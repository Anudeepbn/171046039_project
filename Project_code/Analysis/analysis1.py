import read
import sys
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

#1.Display all the list of companies of particular branch since five years?



def Companies_of_branch(branch):
	sample1=read.sheet2[read.sheet2.Branch==branch]
	samp1=sample1.Company.unique()
	
	s=[]
	for i in samp1:
		if i not in s:
			s.append(i)
	for i in s:
		print(i)

if __name__=='__main__':
	Companies_of_branch(sys.argv[1])