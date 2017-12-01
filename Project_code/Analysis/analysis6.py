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

#6.What is the Percentage of students got placed in Embedded Systems in 2016

def percentage_of_ES_2016():
	sample6=read.sheet1[read.sheet1.Year==2016]
	samp6=sample6[read.sheet1.MscTechProgram=='EmbeddedSystems']
	sam=samp6.Percentage
	print("Percentage of students got placed in Embedded Systems in 2016 is:")
	print(sam)


if __name__=='__main__':
	percentage_of_ES_2016()