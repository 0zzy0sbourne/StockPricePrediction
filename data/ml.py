import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt  , mpld3 
import datetime 
# import scraping 
import sklearn
from sklearn import linear_model , datasets  
from sklearn.metrics import mean_squared_error , r2_score  , mean_absolute_error 
from sklearn.linear_model import LinearRegression 
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor 
from sklearn.tree import DecisionTreeRegressor 




'''
THIS FILE IS TO GET THE DATA FROM THE CSV FILE  AND DRAW GRAPH OF IT AND IMPLEMENT THE POLYNOMİAL REGRESSION ALGORİTHMS 
AND ML ALGORİTHMS . ALSO TO MAKE PREDİCTİONS . 
''' 


# STEP 1 : # load the data from the csv file : .
my_date_parser = lambda x : pd.datetime.strptime(x, "%y-%m-%d" )
my_second_date_parser = lambda x : pd.datetime.strptime(x,"%y/%m/%d")

bitcoinDataFrame = pd.read_csv("bitcoin.csv" ,  sep= ',' ,parse_dates=['Date'] , date_parser = my_date_parser ) 
ethereumDataFrame = pd.read_csv("ethereum.csv", sep = ',' , parse_dates=['Date(UTC)'] , date_parser = my_second_date_parser)
tetherDataFrame = pd.read_csv("tether.csv" , sep = ',' , parse_dates = ['Date'] , date_parser = my_date_parser)
rippleDataFrame = pd.read_csv("ripple.csv" , sep = ',' , parse_dates =['Date'] , date_parser = my_date_parser)
#bitcashDataFrame = pd.read_csv("bitcash.csv"  , sep = ',' , parse_dates = ['Date'] , )



# STEP 2 # plot the data : 

bitx = bitcoinDataFrame["Date"]
bity = bitcoinDataFrame["Open"]

ethx = ethereumDataFrame["Date(UTC)"]
ethy = ethereumDataFrame["Price"]

ripx = rippleDataFrame["Date"]
ripy = rippleDataFrame["Open"]

tetx = tetherDataFrame["Date"]
tety = tetherDataFrame["Open"]


# add the ripple here later !
'''
bitcx = bitcashDataFrame["Date"]
bitcy = bitcashDataFrame["Price"]
'''
# STEP 2 # save your plots : 

plt.plot(bitx , bity)
plt.title('Bitcoin')
plt.savefig("bitcoin.png")


plt.plot(ethx , ethy)
plt.title('Ethereum')
plt.savefig("ethereum.png")
plt.close()

plt.plot(ripx , ripy)
plt.title('Ripple')
plt.savefig("ripple.png")
plt.close()

plt.plot(tetx , tety)
plt.title('Tether')
plt.savefig("tether.png")
plt.close()

'''
plt.plot(bitcx , bitcy)
plt.title('Bitcoin Cash')
plt.savefig("bitcoincash.png")
plt.close()
'''
############## creating a linear model : ########

######BİTCOİN################## 
y_bit  =np.array(bitcoinDataFrame['Open'])

x_bit = np.array(bitcoinDataFrame['Volume'] )
x_bit = x_bit.reshape(-1,1)


bitx_train  , bitx_test  , bity_train  , bity_test = train_test_split(x_bit , y_bit ,random_state = 0 ) ####READ ABOUT THE RANDOM STATE 
bitcoin_model = RandomForestRegressor(random_state = 1 )
bitcoin_model.fit(bitx_train ,  bity_train)
bitcoin_prediction = bitcoin_model.predict(bitx_test)
print("Bitcoin Prediction:")
print(bitcoin_prediction)
## use StandartScaler to feature Scaling .!!!!!!

######################ETHEREUM###################
y_eth  = np.array(ethereumDataFrame['Price'])

x_eth = np.array(bitcoinDataFrame['Volume'] )
x_eth = x_eth.reshape(-1 ,1 )


ethx_train  , ethx_test ,  ethy_train  , ethy_test = train_test_split(x_eth , y_eth , random_state = 0)
ethereum_model = RandomForestRegressor(random_state = 1)
ethereum_model.fit(ethx_train , ethy_train)
ethereum_prediction = ethereum_model.predict(ethx_test)
print("Ethereum Prediction")
print(ethereum_prediction)
#####################TETHER######################33
y_tet = np.array(tetherDataFrame['Open'])

x_tet = np.array(bitcoinDataFrame(['Volume'])
x_tet = x_tet.reshape(-1 , 1)
tetx_train , tetx_test  , tety_train , tety_test = train_test_split(x_tet , y_tet , random_state = 0)
tether_model = RandomForestRegressor(random_state = 1 )
tether_model.fit(tetx_train , tety_train)
tether_prediction = tether_model.predict(tetx_test)
print(tether_prediction)
####################BİTCASH############################3
y_bitc = np.array(bitcashDataFrame['Open'])

x_bitc = np.array(bitcoinDataFrame['Volume'])
x_bitc = x_bitc.reshape(-1 , 1 )
bitcx_train  , bitcx_test  , bitcy_train , bitcy_test = train_test_split(x_bitc , y_bitc , random_state = 0)  
bitcash_model = RandomForestRegressor(random_state = 1)
bitcash_model.fit(bitcx_train , bitcy_train)
bitcash_prediction = bitcash_model.predict(bitcx_test)
print(bitcash_prediction)
# matrices are okay . 




