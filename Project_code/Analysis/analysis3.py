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



#3.List out all the student required details of Bigdata-2016


def All_Bigdata():
	sample3=read.sheet2[read.sheet2.Year==2016]
	sam3=sample3[read.sheet2.Branch=='BDA'][['BE (BRANCH)','BE_Aggregate','I Sem GPA','Company','Stipend']]
	print(sam3)


if __name__=='__main__':
	All_Bigdata()