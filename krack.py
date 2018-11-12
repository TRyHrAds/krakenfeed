# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 08:27:34 2018

@author: mnunes
"""

import datetime as dt

import krakenex



incremental_update=True



class KrakenFeeder:
    def __init__(self, TradablePairs):
        self._TradablePairs=TradablePairs
        
        self._all_spot_pricesi={}
        self._carbon_header='syss.crypto.'
        self._rt_moniker='{}{}'.format(self._carbon_header,'realtime')
        self._k=krakenex.API()
    def publish(self):
        try:
           
            now=dt.datetime.utcnow()
            for pair in self._TradablePairs:
                spot_price=self._k.query_public('Depth',{'pair':pair,'count':'5'})
               # print(spot_price.keys())
                if 'result' in spot_price.keys():
                    spot_pricei=spot_price['result'][pair]
    
                    mid=(float(spot_pricei['asks'][0][0])+float(spot_pricei['bids'][0][0]))/2.0
              
                    print('{}: {} published -{}'.format(pair,mid,now))
                else:
                    print('did not succ {} prices from Kraken - {}'.format(pair,now))
        except:
            pass
        
        
        


                
TradablePairs=['XETHZUSD','XXBTZUSD','XXRPZUSD']




krakenfeeder=KrakenFeeder(TradablePairs)

while(True):
    try:
        krakenfeeder.publish()
    except:
        continue