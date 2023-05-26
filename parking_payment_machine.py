from datetime import datetime
import math
def money_balance(usertotal,total):#計算餘額(找零)
    givechange=usertotal-total 
    if givechange<0:
        print("金額不足",-givechange)
        return False
    else:
        return givechange
def parking_costs(five,ten,fifty,fake_5,fake_10,fake_50):#使用者投入的硬幣
    if fake_5>0 or fake_10>0 or fake_50>0:#偵測到非法硬幣時回傳false
        return False
    else:
        usertotal=five*5+ten*10+fifty*50
        return usertotal
def displayparking_time(pstart,pend):#顯示停車時間
    ptime=pend-pstart
    days=ptime.days
    hours=ptime.seconds//3600
    min=(ptime.seconds%3600)//60
    print(f"共停了{days}天{hours}小時{min}分")    
def parking_times(pstart,pend):#計算停車時間費用(計算有幾個半小時)
    ptime=(pend-pstart).total_seconds()//60/30
    pt=math.ceil(ptime)
    return pt
def parking_wday(parking_time,wday):#判斷平日和假日
    if wday>=0 and wday<=4:#平日計費
        total=parking_time*15
        if total>=300:#平日單日最高計費300
            total=300
    else:
        total=parking_time*20#假日計費
        if total>=420:#假日單日最高計費420
            total=420
    return total
def parking_money(pstart,pend):#計算停車費
    total=0
    I_wday=pstart.weekday()#進場星期
    O_wday=pend.weekday()#退場星期
    if I_wday==O_wday:#當日停車
        wday = I_wday=O_wday
        parking_time=parking_times(pstart,pend)#計算停車時間
        total=parking_wday(parking_time,wday)#計算停車費用(判斷是假日或是平日)
    else:# 跨日停車
        # 計算第一天停車費用
        wday = I_wday
        next_day_start=datetime(pstart.year,pstart.month,pstart.day+1) 
        parking_time=parking_times(pstart,next_day_start)
        total += parking_wday(parking_time,wday)#計算停車費用(判斷是假日或是平日)
        # 計算中間整天停車費用
        for i in range((pend-next_day_start).days):
            wday = (wday + 1) % 7#判斷星期幾
            total +=parking_wday(24*60//30,wday)#計算停車費用(判斷是假日或是平日)
        # 計算最後一天停車費用
        wday=O_wday
        parking_time=parking_times(datetime(pend.year,pend.month,pend.day),pend)
        total+= parking_wday(parking_time,wday)#計算總停車費
    return total    
def parking_payment_machine(carnum,five,ten,fifty,fake_5,fake_10,fake_50,pstart,pend):#停車場繳費系統
    displayparking_time(pstart,pend)#顯示停車時間
    givechange=0
    total=parking_money(pstart,pend)
    usertotal=parking_costs(five,ten,fifty,fake_5,fake_10,fake_50)#計算投入金額
    givechange=money_balance(usertotal,total)#找錢
    if givechange==False:
        print("金額錯誤取消付款")
        print("退還已投入金額",f"${five}枚5元{ten}枚10元{fifty}枚50元") 
    elif usertotal==False:
        print("偵測到非法硬幣")
        print("退還已投入金額",f"${five}枚5元{ten}枚10元{fifty}枚50元")    
    else:        
        print("車號",carnum)
        print("停車費共",total,"元","投入金額",usertotal,"找",givechange,"元")
parking_start=datetime(2023,5,25,23,0)
parking_end=datetime(2023,5,25,23,1)
parking_payment_machine(512,0,3,1,0,0,0,parking_start,parking_end)
parking_start = datetime(2023,5,25,0,0)
parking_end = datetime(2023,5,27,5,0)
parking_payment_machine(512,0,0,100,0,0,0,parking_start,parking_end)

#單元測試
#找零功能測試(3pass)
def test_unit_money_balance():
    assert money_balance(1000,100)==900#投入1000 停車費100 找900
def test_unit_money_balance1():
    assert money_balance(50,30)==20#投入50 停車費30 找20
def test_unit_money_balance2():
    assert money_balance(100,100)==0#投入100 停車費100 找0    
#找零功能錯誤測試(3 fail) 
def test_unit_money_balance3():
    assert money_balance(50,100)==-50#投入50 停車費100 回傳false
def test_unit_money_balance4():
    assert money_balance(0,100)==-100#投入0 停車費100 回傳false
def test_unit_money_balance5():
    assert money_balance(1000,100)==1100 #投入1000 停車費100 找900    
#使用者投入硬幣測試(5 pass)
def test_unit_parking_costs():
    assert parking_costs(1,1,0,0,0,0)==15#投入5元*1 10元*1 50元*0 共投入15元
def test_unit_parking_costs0():
    assert parking_costs(1,0,1,0,0,0)==55#投入5元*1 10元*0 50元*1 共投入55元    
def test_unit_parking_costs1():
    assert parking_costs(1,1,1,0,0,0)==65#投入5元*1 10元*1 50元*1 共投入65元
def test_unit_parking_costs2():
    assert parking_costs(1,1,1,1,0,0)==False#投入5元*1 10元*1 50元*1 非法硬幣5元 偵測到非法硬幣回傳false    
def test_unit_parking_costs3():
    assert parking_costs(1,1,20,0,0,0)==1015#投入5元*1 10元*1 50元*20 共投入1015元
#使用者投入硬幣錯誤測試(3 fail)
def test_unit_parking_costs4():
    assert parking_costs(0,0,0,1,1,0)==15#投入非法5元*1 非法10元*1  共投入15元
def test_unit_parking_costs5():
    assert parking_costs(0,0,0,1,0,0)==5#投入非法5元*1  共投入5元
#計算停車費
def test_unit_parking_money():
    test_s=datetime(2023,5,25,23,0)
    test_e=datetime(2023,5,25,23,1)
    assert parking_money(test_s,test_e)==15#平日停一分鐘 共15元
def test_unit_parking_money1():
    test_s=datetime(2023,5,21,23,0)
    test_e=datetime(2023,5,22,23,0)
    assert parking_money(test_s,test_e)==340#假日(21號)1小時40+ 平日(22號)23小時300 共340
def test_unit_parking_money2():
    test_s=datetime(2023,5,21,23,0)
    test_e=datetime(2023,5,23,0,1)
    assert parking_money(test_s,test_e)==355#假日(21號)1小時40+ 平日(22號整天)300+平日(23號)1分15 共355        
     
