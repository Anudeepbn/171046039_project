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

#2.List out all the students who got placed in Intel, Bangalore in VLSI  2015

def intel_Placed_vlsi():
	sample2=read.sheet2[read.sheet2.Branch=='VLSI']
	sam2=sample2[read.sheet2.Company=='Intel, Bangalore']
	sam3=sam2[read.sheet2.Year==2015]
	print(sam3)

if __name__=='__main__':
	intel_Placed_vlsi()