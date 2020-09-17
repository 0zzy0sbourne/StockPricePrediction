import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import datetime 
# import scraping 
import sklearn
from sklearn import linear_model , datasets  
from sklearn.metrics import mean_squared_error , r2_score  , mean_absolute_error 
from sklearn.linear_model import LinearRegression 
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler , MinMaxScaler 
from sklearn.ensemble import RandomForestRegressor 
from sklearn.tree import DecisionTreeRegressor 
import seaborn as sns 


# feature normalization function  
def normalizeData(df): 
    min_max_scaler = sklearn.preprocessing.MinMaxScaler()
    df['Open'] = min_max_scaler.fit_transform(df.open.values.reshape(-1 ,1 ))
    df['Close'] = min_max_scaler.fit_transform(df.close.values.reshape(-1,1))
    df['Low'] = min_max_scaler.fit_transform(df.low.value.reshape(-1 ,1))
    df['High'] = min_max_scaler.fit_transform(df.high.value.reshape(-1 , 1)) 
    return df


def convert_astype(columnList  , df): 
    for i in columnList: 
        if type(df[i].head(1)) =="object": 
            print("yes") 


def plotSaveData(df , coinName ) :  # not for ethereum . 
    figs = [] # empty list to keep price and volume plot.
    fig1= plt.figure(figsize= (15 ,5)); 
    plt.subplot(1 ,2  ,1); 
    df.plot(x = 'Date' , y = ['Open' ,'Close' , 'Low' , 'High'] )
    plt.title(coinName)
    plt.xlabel('Date')
    plt.ylabel('Prices')
    figs.append(fig1)
    if coinName == "Bitcoin" :
        plt.savefig('/home/ozan/Desktop/Git/python/venv/application/bitcoinPriceFig.png')
    elif coinName == "Tether" :
        plt.savefig('/home/ozan/Desktop/Git/python/venv/application/tetherPriceFig.png')
   
    elif coinName == "Ripple": 
        plt.savefig('/home/ozan/Desktop/Git/python/venv/application/ripplePriceFig.png')
   
    plt.close(fig1)

    
    '''
    plt.plot(df['Open'].values ,  color = 'red' , label='open' )
    plt.plot(df['Close'].values , color = 'green' , label = 'close')
    plt.plot(df['Low'].values  , color ='blue' , label = 'low')
    plt.plot(df['High'].values , color = 'black'   , label = 'high') 
    plt.title(coinName)
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend(loc= 'best')
    plt.show()
'''

    fig2 = plt.figure(figsize=(15,5)); 
    plt.subplot(1,2,2); 
    df.plot(x='Date' , y = 'Volume')
    plt.title(coinName)
    plt.xlabel('Date')
    plt.ylabel('Volume')
    plt.legend(loc ='best')
    figs.append(fig2)
    if coinName == "Bitcoin" :
       plt.savefig('/home/ozan/Desktop/Git/python/venv/application/bitcoinVolumeFig.png')
    elif coinName == "Tether" :
       plt.savefig('/home/ozan/Desktop/Git/python/venv/application/tetherVolumeFig.png')
   
    elif coinName == "Ripple": 
       plt.savefig('/home/ozan/Desktop/Git/python/venv/application/rippleVolumeFig.png')
    
    plt.close(fig2)
    return figs 
    
def plotEthereum(df): 
    # date , unixtimestamp , supply ,  Marketcap , Price . 
     # marketcap = supply * price . 
    fig = plt.figure(figsize = (15 ,  5)); 
    plt.subplot( 1,2,1) ; 
    df.plot(x = 'Date(UTC)' , y=['MarketCap' , 'Price'])
    '''
    plt.plot(df['MarketCap'].values , color ='blue' , label = 'MarketCap')
    plt.plot(df['Price'].values , color = 'red' , label = 'Price')
    '''
    plt.title('Ethereum')
    plt.xlabel('Time')
    plt.ylabel('Price & MaketCap')
    plt.legend(loc='best')
    plt.savefig('/home/ozan/Desktop/Git/python/venv/application/Ethereum.png')
    plt.close(fig)
    

# load the data : 
bitcoinDataFrame= pd.read_csv('bitcoin.csv')
etherDataFrame = pd.read_csv('ethereum.csv')
tetherDataFrame = pd.read_csv('tether.csv')
rippleDataFrame = pd.read_csv('ripple.csv')
bitcashDataFrame = pd.read_csv('bitcash.csv') 
pd.to_datetime(bitcoinDataFrame['Date'])
pd.to_datetime(etherDataFrame['Date(UTC)'])
pd.to_datetime(bitcashDataFrame['Date'])
pd.to_datetime(rippleDataFrame['Date'])
pd.to_datetime(tetherDataFrame['Date'])

# STEP 2 # plot the data : 
plotSaveData(bitcoinDataFrame , "Bitcoin" )

plotSaveData(tetherDataFrame , "Tether")
plotEthereum(etherDataFrame) # looks like it does not work .
############## creating a linear model : ########
'''

bitcoinDataFrame = bitcoinDataFrame.dropna()
y_bit = bitcoinDataFrame[["Open"]]
x_bit = bitcoinDataFrame[["Volume"]]


bit_lm = LinearRegression() 
bit_model = bit_lm.fit(x_bit , y_bit)
bitcoinPrediction = bit_model.predict(x_bit)
MSE = mean_squared_error(y_bit , bitcoinPrediction)
RMSE = np.sqrt(MSE)
# RMSE is 2968






'''
'''
######BİTCOİN################## 
y_bit  =np.array(bitcoinDataFrame['Price'])

x_bit = np.array(bitcoinDataFrame['Change'])
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

x_eth = np.array(bitcoinDataFrame['Change'])
x_eth = x_eth.reshape(-1 ,1 )


ethx_train  , ethx_test ,  ethy_train  , ethy_test = train_test_split(x_eth , y_eth , random_state = 0)
ethereum_model = RandomForestRegressor(random_state = 1)
ethereum_model.fit(ethx_train , ethy_train)
ethereum_prediction = ethereum_model.predict(ethx_test)
print("Ethereum Prediction")
print(ethereum_prediction)
#####################TETHER######################33
y_tet = np.array(tetherDataFrame['Price'])

x_tet = np.array(bitcoinDataFrame['Change'])
x_tet = x_tet.reshape(-1 , 1)
tetx_train , tetx_test  , tety_train , tety_test = train_test_split(x_tet , y_tet , random_state = 0)
tether_model = RandomForestRegressor(random_state = 1 )
tether_model.fit(tetx_train , tety_train)
tether_prediction = tether_model.predict(tetx_test)
print(tether_prediction)
####################BİTCASH############################3
y_bitc = np.array(bitcashDataFrame['Price'])

x_bitc = np.array(bitcoinDataFrame['Change'])
x_bitc = x_bitc.reshape(-1 , 1 )
bitcx_train  , bitcx_test  , bitcy_train , bitcy_test = train_test_split(x_bitc , y_bitc , random_state = 0)  
bitcash_model = RandomForestRegressor(random_state = 1)
bitcash_model.fit(bitcx_train , bitcy_train)
bitcash_prediction = bitcash_model.predict(bitcx_test)
print(bitcash_prediction)
# matrices are okay . 
'''



