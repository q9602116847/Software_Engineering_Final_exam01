from datetime import datetime
def money_balance(usertotal,total):#計算餘額(找零)
    if usertotal-total<0:
        print("金額不足")
        givechange=0
    else:
        givechange=usertotal-total    
    return givechange
def parking_costs(five,ten,fifty):#使用者投入的硬幣
    usertotal=five*5+ten*10+fifty*50
    return usertotal
def parking_times(pstart,pend):#計算停車時間
    ptime=(pend-pstart).seconds
    return (ptime/60//30)+1
def parking_money(parking_time,wday):#判斷平日和假日
    if wday>=0 and wday<=4:#平日計費
        total=parking_time*15
        if total>=300:
            total=300
    else:
        total=parking_time*20#假日計費
        if total>=420:
            total=420
    return total
def parking_payment_machine(carnum,five,ten,fifty,pstart,pend):
    I_wday=pstart.weekday()#進場星期
    O_wday=pend.weekday()#退場星期
    total=0
    givechange=0
    if I_wday==O_wday:#當日停車
        wday = I_wday
        parking_time=parking_times(pstart,pend)#計算停車時間
        total=parking_money(parking_time,wday)#計算停車費用
        usertotal=parking_costs(five,ten,fifty)#計算投入金額
    else:# 跨日停車
        # 計算第一天停車費用
        wday = I_wday
        next_day_start=datetime(pstart.year,pstart.month,pstart.day+1) 
        parking_time=parking_times(pstart,next_day_start)
        total += parking_money(parking_time,wday)
        # 計算中間整天停車費用
        for i in range((pend-next_day_start).days):
            wday = (wday + 1) % 7#判斷星期幾
            total +=parking_money(24*60//30,wday)
        # 計算最後一天停車費用
        wday=O_wday
        parking_time=parking_times(datetime(pend.year,pend.month,pend.day),pend)
        total+= parking_money(parking_time,wday)#計算總停車費
        usertotal=parking_costs(five,ten,fifty)#計算投入金額
    givechange=money_balance(usertotal,total)#找錢    
    print("車號",carnum)
    print("停車費共",total,"元","投入金額",usertotal,"找",givechange,"元")
parking_start=datetime(2023,5,25,23,8)
parking_end=datetime(2023,5,25,23,10)
parking_payment_machine(512,0,3,1,parking_start,parking_end)
parking_start = datetime(2023,5,25,1,30)
parking_end = datetime(2023,5,27,4,30)
parking_payment_machine(512,0,0,100,parking_start,parking_end)
def test_answer():
    assert parking_payment_machine(512,0,3,1,parking_start,parking_end) 
