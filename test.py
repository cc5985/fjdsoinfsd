'''
account: represents account

'''


# coding=utf-8
from OkcoinSpotAPI import OKCoinSpot
from OkcoinFutureAPI import OKCoinFuture
import account
import currency_pair
import okex

market="OKEx"
account=account.Account("test")
okex1=okex.OKEx(account)
currency_pair_of_bch_usdt=currency_pair.CurrencyPair('bch','usdt').get_currency_pair()

# 初始化apikey，secretkey,url
# print(account.api_key,account.secret_key,account.name)

# currency_pair1=currency_pair.CurrencyPair()
# currency_pair1=currency_pair1.get_currency_pair()
#
# print(currency_pair1)


'''
the following are http.get test
----------------------------------------------------------------------------
# test for ticker function:                                                 
# print(currency_pair_of_bch_usdt)                                          
# ticker=okex1.ticker(currency_pair_of_bch_usdt)                            
# print(ticker)                                                             

# test for depth function:
# depth=okex1.depth(currency_pair_of_bch_usdt)
# print(depth)

# test for trades function, this function might be obsolete in the current API:
# trades=okex1.trades(currency_pair_of_bch_usdt)
# print(trades)
----------------------------------------------------------------------------
'''

'''
the following are http.post test
----------------------------------------------------------------------------
# test for balances function:
# balances=okex1.balances()
# print(balances)

# test for submit_order function, as in OKcoinSpotAPI it is known as trade:
# result=okex1.submit_order("sell","bch_usdt",10000,0.01)
# print(result)

# 98104990
# test for cancel_order function, as in OKcoinSpotAPI it is known as ...:
# result=okex1.cancel_order(currency_pair_of_bch_usdt,98104990)
# print(result)

# order_list这个方法是取得未成交订单的列表！
# test for order_list function:
# result=okex1.order_list(currency_pair_of_bch_usdt)
# print(result)

# trade_list这个方法是取得已成交订单的列表！
# test for trade_list function:
# result=okex1.trade_list(currency_pair_of_bch_usdt)
# print(result)

# 以下是独享的方法
# test for batch_trade
# result=okex1.batch_trade(currency_pair_of_bch_usdt,"buy","[{price:10001.1,amount:0.01,type:'sell'},{price:10002.2,amount:0.01,type:'sell'}]")
# print(result)
----------------------------------------------------------------------------
'''

'''
----------------------------------------------------------------------------
# test for json management
# import universal
# result=okex1.order_list(currency_pair_of_bch_usdt)
# print(result)
# result=okex1.cancel_order(currency_pair_of_bch_usdt,98179657)
# cancel_order_result1=universal.CancelOrderResult("OKEx",currency_pair_of_bch_usdt,result,98179657)
# print(cancel_order_result1)

# test for universal.Depth class and whose functions:
# import universal
# import copy
# depth=okex1.depth(currency_pair_of_bch_usdt)
# depth1=universal.Depth("OKEx",currency_pair_of_bch_usdt,depth)
# depth2=copy.deepcopy(depth1)
# depth_diff=depth1-2
# print(depth_diff)
----------------------------------------------------------------------------
'''

'''
test for universal module:
----------------------------------------------------------------------------
import universal
# test for ticker function:
# ticker=okex1.ticker(currency_pair_of_bch_usdt)
# print(ticker)
# print(ticker.__class__)

# test for depth function:
# depth=okex1.depth(currency_pair_of_bch_usdt)
# print(depth)

# test for trades function, this function might be obsolete in the current API:
# trades=okex1.trades(currency_pair_of_bch_usdt)
# trades=universal.Trades(market,currency_pair_of_bch_usdt,trades,2)
# print(trades)
----------------------------------------------------------------------------
'''

# test for universal module2:
import universal

# test for balances function:
# balances=okex1.balances()
# print(balances)

# test for submit_order function, as in OKcoinSpotAPI it is known as trade:
# result=okex1.submit_order("sell","bch_usdt",10000,0.01)
# print(result)

# 98104990
# test for cancel_order function, as in OKcoinSpotAPI it is known as ...:
# result=okex1.cancel_order(currency_pair_of_bch_usdt,98104990)
# print(result)

# order_list这个方法是取得未成交订单的列表！
# test for order_list function:
# result=okex1.order_list(currency_pair_of_bch_usdt)
# print(result)

# trade_list这个方法是取得已成交订单的列表！
# test for trade_list function:
# result=okex1.trade_list(currency_pair_of_bch_usdt)
# print(result)

# 以下是独享的方法
# test for batch_trade
# result=okex1.batch_trade(currency_pair_of_bch_usdt,"buy","[{price:10001.1,amount:0.01,type:'sell'},{price:10002.2,amount:0.01,type:'sell'}]")
# print(result)