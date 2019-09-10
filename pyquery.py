#pip install pyquery

search_coin = ""
search_coin = "\u82F1\u938A" #@param ["\u7F8E\u91D1", "\u6E2F\u5E63", "\u82F1\u938A", "\u6FB3\u5E63", "\u52A0\u62FF\u5927\u5E63", "\u65B0\u52A0\u5761\u5E63", "\u745E\u58EB\u6CD5\u90CE", "\u65E5\u5713", "\u5357\u975E\u5E63"]
from pyquery import PyQuery

TwnBANK = PyQuery("https://rate.bot.com.tw/xrt?Lang=zh-TW")

#幣別
coin_names = TwnBANK('div.hidden-phone').text().split()

#現金匯率-本行買入
coin_Buyin1 = TwnBANK('td.rate-content-cash[data-table="本行現金買入"]').text().split()

#現金匯率-本行賣出
coin_Buyout1 = TwnBANK('td.rate-content-cash[data-table="本行現金賣出"]').text().split()

#print(coin_names)
#print(coin_Buyin1)
#print(coin_Buyout1)

TwnBANK_dic = {}

price_idx = 0
for idx, name in enumerate(coin_names):
    if idx % 2 == 0:
        TwnBANK_dic[name] = {
            "bids" : coin_Buyin1[price_idx],
            "offers" : coin_Buyout1[price_idx]
        }
        price_idx += 1
        
#print(TwnBANK_dic)

search_coin = input("請輸入要查詢的貨幣")

def show_Msg (name):
        bids = TwnBANK_dic[name]["bids"]
        offers = TwnBANK_dic[name]["offers"] 
        return("{0}\t本行現金買入 : {1} \t本行現金賣出 : {2}".format(name,bids,offers))

print(show_Msg(search_coin))