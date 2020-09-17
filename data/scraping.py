'''
WE HAVE GOT SELENIUM AND BS4 
'''
import csv
import numpy as np 
import pandas as pd 
from bs4 import BeautifulSoup 
from selenium import webdriver 
import time 
import re
import schedule
import datetime 
import sys






def myProgram(): 


    now = datetime.datetime.now()




    def write_to_file( file_name , price , change , date):
        with open(file_name , 'a' )  as csv_file:
            fnames = ['Price' , 'Change' , 'Date']
            writer = csv.DictWriter(csv_file , fieldnames=fnames ) 
            writer.writerow({'Price' : price , 'Change' : change  , 'Date' : date  })

   

    investing = "https://tr.investing.com/"

    process = 0  



    # start web browser
    browser=webdriver.Firefox()

    # get source code6
    browser.get(investing)
    html = browser.page_source
    time.sleep(2)

    soup = BeautifulSoup(html , 'html.parser')
    CurrencyNames = soup.find_all('td' , {"class" :'left bold elp name cryptoName first js-currency-name'} ) 

    regex1 = re.compile('.*pid.*')
    CurrencyPrices = soup.find_all('a' , {"class" : regex1})  

    regex2 = re.compile('.*js-currency-change-24h.*')
    CurrencyChanges = soup.find_all('td' , {"class" : regex2})





    # close web browser
    browser.close()




    Names = []
    for name in CurrencyNames : 
        Names.append(name.get_text())

    Prices = []
    for price in CurrencyPrices: 
        Prices.append(price.get_text()) 

    Changes = [] 
    for change in CurrencyChanges : 
        Changes.append(change.get_text())





    # generate a initial numpy array if csv file is empty: 
    #and if it is not empty , append the new data to the numpy array . 
    bitcoin_change = np.array([Changes[0]])
    bitcoin_price = np.array([Prices[0]])



    ethereum_change = np.array([Changes[1]])
    ethereum_price = np.array([Prices[1]])

  

    ripple_change = np.array([Changes[2]])
    ripple_price = np.array([Prices[2]]) 

 
    tether_change = np.array([Changes[3]])
    tether_price = np.array([Prices[3]]) 

 
    bitcoincash_change = np.array([Changes[4]])
    bitcoincash_price = np.array([Prices[4]])

   
    write_to_file("bitcoin.csv" , Prices[0]  , Changes[0] , now )  
    write_to_file("ethereum.csv" , Prices[1] , Changes[1]  , now )
    write_to_file("tether.csv" , Prices[2] ,  Changes[2] , now )
    write_to_file("ripple.csv " , Prices[3] , Changes[3]  , now )
    write_to_file("bitcoincash.csv" , Prices[4] , Changes[4] , now )




    process += 1 







    '''
    gets the instance data from the website and writes it into the CSV file . 
    '''



def exit(): 
    sys.exit()


schedule.every().day.at("17:13").do(myProgram)
schedule.every().day.at("17:14").do(exit) 


while 1: 
    schedule.run_pending() 
    time.sleep(5)
    

