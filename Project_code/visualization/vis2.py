import read
'''import pandas as pd
'''
import numpy as np

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

##2.Show the Visualization for the placement in all the branch_class in 2013

sample3=read.sheet1[read.sheet1.Year==2013]
samp3=sample3.TotalClassStrength
#print(samp3)
##
sample4=read.sheet1[read.sheet1.Year==2013]
samp4=sample4.TotalPlacedStudent
#print(samp4)

def placement_allbranch_2013():
	N=8
	class_strength=samp3
	#strength_std=np.random.randint(2,10,8)
    
	ind=np.arange(N)
	width=0.35
	
	fig,ax=plt.subplots()
	rect1=ax.bar(ind,class_strength,width)#,color="r")#,yerr=strength_std)

	class_placed=samp4
	#placed_std=np.random.randint(2,10,8)
	
	rect2=ax.bar(ind+width,class_placed,width)#,color="y")#,yerr=placed_std)
	
	#plt.ylable('stastics')
	plt.title('stastics of placed in 2013')
	plt.xticks(ind+width/2)
	plt.xticks(ind+width,('MS','VLSI','ES(BE)','ES(BCA)','VLSI(vrft)','EW','IT','CT&V','Total'))
	plt.xlabel('Branches')
	plt.legend(('class_strength','class_placed'))
	
	plt.show()

if __name__=='__main__':
	placement_allbranch_2013()