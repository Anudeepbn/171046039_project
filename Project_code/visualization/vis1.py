import read
'''import pandas as pd

import numpy as np
'''
import matplotlib.pyplot as plt

'''
#### read excel sheet

sheet1= pd.read_excel('Placementsois.xlsx',sheetname='placementstats')


sheet2= pd.read_excel('Placementsois.xlsx',sheetname='enrollment')


sheet1_reindexing=sheet1.reset_index()
'''
##################################
###Visualization
####

##1.Show the Visualization of Percantage of placement of all branches in 2016


sample1=read.sheet1[read.sheet1.Year==2016]
samp1=sample1.Percentage
#sam=samp1.Percentage
#samp1=filter(None,samp1)

#print(samp1)
####
sample2=read.sheet1[read.sheet1.Year==2016]
samp2=sample2.MscTechProgram
#print(samp2)

forsize1=read.sheet1[read.sheet1.Year==2016]
forsz1=forsize1.Percentage
#print(forsz1)
##

def Percentage_placement_2016():
	labels=samp1	


	sizes=forsz1

	#colors = ['gold', 'yellowgreen', 'lightcoral','lightskyblue','pink','darkblue','white','yellow','red','lightgreen']
	
	explode = (0.02, 0.02, 0.02, 0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02)  # exploding all slice
	# Plot
	#plt.pie(sizes, explode=explode,labels=labels,autopct='%1.1f%%', startangle=140)
	plt.pie(sizes, explode=explode,labels=labels,startangle=140)	
	leg=samp2
	#plt.legend(leg,loc="upper right",bbox_to_anchor=(0.5,0.5,0.5,0.5))
	plt.legend(leg,loc="upper right",ncol=1,fancybox=True)
    #plt.sizeslables(100,100,90.48,90,100,100,0.0,100,100)
	plt.axis('equal')
	plt.show()

if __name__=='__main__':
	Percentage_placement_2016()