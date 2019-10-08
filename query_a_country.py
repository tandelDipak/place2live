import pandas as pd
import numpy as np
import os
df=pd.read_csv(os.getcwd()+"/city/output/list_of_countries.csv")
df.set_index("country",inplace = True )
print("Enter the name of a country : ",end=" ")
country_to_be_searched=input().title()
try:
	for i in df:
		if(not np.isnan(df.loc[country_to_be_searched][str(i)])):
			print(i,df.loc[country_to_be_searched][str(i)])	
except:
	print("Country name is absent in database.")
