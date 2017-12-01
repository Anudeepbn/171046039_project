import read

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

##Dispaly stastics all year of palcements took in SOIS department

sample5=read.sheet1[read.sheet1.MscTechProgram=='TOTAL']
#samp5=sample5[sheet1.TotalClassStrength]
samp5=sample5.TotalClassStrength
#print(samp5)
###
sample6=read.sheet1[read.sheet1.MscTechProgram=='TOTAL']
#samp5=sample5[sheet1.TotalClassStrength]
samp6=sample6.TotalPlacedStudent
#print(samp5)


def stastics_of_all_year():
	N=4
	total_strength=samp5
	#strength_std=np.random.randint(2,10,8)
    
	ind=np.arange(N)
	width=0.35
	
	fig,ax=plt.subplots()
	rect1=ax.bar(ind,total_strength,width,color="r")#,yerr=strength_std)

	total_placed=samp6
    #placed_std=np.random.randint(2,10,8)
	
	rect2=ax.bar(ind+width,total_placed,width,color="y")#,yerr=placed_std)
	
	#plt.ylable('stastics')
	plt.title('stastics of placed in 2013')
	#plt.xticks(ind+width/2)
	plt.xticks((ind+width/2),('2013','2014','2015','2016'))
	plt.xlabel('Branches')
	plt.ylabel('total students')
	plt.legend(('total_strength','total_placed'))
	
	plt.show()
	

if __name__=='__main__':
	stastics_of_all_year()