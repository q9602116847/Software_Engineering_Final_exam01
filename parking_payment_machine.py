from datetime import datetime
import math
def Input_car_number(carnum):#輸入車牌
    cardatabase={"ABC-1234","QWE-1234","IC8-7630","B567-9010"}#假設停車場有這些車輛
    if carnum in cardatabase:
        return True
    else:
        print("找不到此車牌")
    return False    
def money_balance(usertotal,total):#計算餘額(找零)
    if usertotal!=0 and usertotal>=total:
        givechange=usertotal-total
    else:
        givechange=0     
    return givechange
def parking_costs(five,ten,fifty,fake_5,fake_10,fake_50):#使用者投入的硬幣
    if fake_5>0 or fake_10>0 or fake_50>0:#偵測到非法硬幣時回傳false
        return False
    else:
        usertotal=five*5+ten*10+fifty*50
        return usertotal
def displayparking_time(pstart,pend):#顯示停車時間
    print(f"進場時間為{pstart}")
    print(f"離場時間為{pend}")
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
        parking_time=parking_times(pstart,pend)#呼叫計算停車時間函式
        total=parking_wday(parking_time,wday)#呼叫計算停車費用(判斷是假日或是平日)
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
def check(usertotal,total,five,ten,fifty):
    if usertotal==False&usertotal!=0:
        print("偵測到非法硬幣")
        if five>0 or ten>0 or fifty>0:
            print("退還已投入金額",f"${five}枚5元{ten}枚10元{fifty}枚50元")
        total=0
        return False
    elif total>usertotal:
        print("付款金額錯誤")
        print(f"差{total-usertotal}元")
        print("取消付款!!")
        if five>0 or ten>0 or fifty>0:
            print("退還已投入金額",f"${five}枚5元{ten}枚10元{fifty}枚50元")
        return False        
    else:
        givechange=0
        givechange=money_balance(usertotal,total)#找錢
        print("停車費共",total,"元","投入金額",usertotal,"找",givechange,"元")
        return True
    
def parking_payment_machine(carnum,five,ten,fifty,fake_5,fake_10,fake_50,pstart,pend):#停車場繳費系統
    print("-----------------------------------------------------------")
    iscarnum=Input_car_number(carnum)
    if iscarnum==False:
        print("查無此車牌 需輸入完整的車牌號碼")
        return False#查無車牌取消付款
    else:
        print("-----------------------------------------------------------")
        print("車牌號碼",carnum)
        displayparking_time(pstart,pend)#顯示停車時間
        total=parking_money(pstart,pend)
        usertotal=parking_costs(five,ten,fifty,fake_5,fake_10,fake_50)#計算投入金額
        settlement=check(usertotal,total,five,ten,fifty)
        print("-----------------------------------------------------------")
        return settlement
parking_start=datetime(2023,5,25,23,0)
parking_end=datetime(2023,5,25,23,1)
parking_payment_machine("ABC-1234",0,0,0,0,0,0,parking_start,parking_end)
parking_start = datetime(2023,5,25,0,0)
parking_end = datetime(2023,5,27,5,0)
parking_payment_machine("IC8-7630",0,0,100,0,0,0,parking_start,parking_end)
parking_payment_machine("I",0,0,100,0,0,0,parking_start,parking_end)
#單元測試
#找零功能測試(3 pass)
def test_unit_money_balance():
    assert money_balance(1000,100)==900#投入1000 停車費100 找900
def test_unit_money_balance0():
    assert money_balance(50,30)==20#投入50 停車費30 找20
def test_unit_money_balance1():
    assert money_balance(100,100)==0#投入100 停車費100 找0    
#找零功能錯誤測試(3 fail) 
def test_unit_money_balance2():
    assert money_balance(50,100)==50#投入50 停車費100 回傳0
def test_unit_money_balance3():
    assert money_balance(0,100)==-100#投入0 停車費100 回傳0
def test_unit_money_balance4():
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
    assert parking_costs(0,0,0,1,1,0)==15#投入非法5元*1 非法10元*1  共投入15元 回傳False
def test_unit_parking_costs5():
    assert parking_costs(0,0,0,1,0,0)==5#投入非法5元*1  共投入5元 回傳False
#計算停車費(3 pass)
def test_unit_parking_money():
    test_s=datetime(2023,5,25,23,0)
    test_e=datetime(2023,5,25,23,1)
    assert parking_money(test_s,test_e)==15#平日停1分鐘 共15元
def test_unit_parking_money0():
    test_s=datetime(2023,5,21,23,0)
    test_e=datetime(2023,5,22,23,0)
    assert parking_money(test_s,test_e)==340#假日(5/21)1小時40+ 平日(5/22)23小時300 共340元
def test_unit_parking_money1():
    test_s=datetime(2023,5,21,23,0)
    test_e=datetime(2023,5,23,0,1)
    assert parking_money(test_s,test_e)==355#假日(5/21)1小時40+ 平日(5/22號)300+平日(5/23)1分15 共355元        
#計算停車費錯誤測試(2 fail)
def test_unit_parking_money2():
    test_s=datetime(2023,4,1,23,0)
    test_e=datetime(2023,4,1,23,1)
    assert parking_money(test_s,test_e)==15#假日(4/1)1分鐘 20元
def test_unit_parking_money3():
    test_s=datetime(2023,4,2,23,25)
    test_e=datetime(2023,4,2,23,56)
    assert parking_money(test_s,test_e)==20#假日(4/2)31分鐘 400元
#輸入車牌測試(4 pass)需輸入完整的車牌號碼   
def test_unit_carnumber():
    carnum="ABC-1234"
    assert Input_car_number(carnum)==True
def test_unit_carnumber0():
    carnum="QWE-1234"
    assert Input_car_number(carnum)==True
def test_unit_carnumber1():
    carnum="IC8-7630"
    assert Input_car_number(carnum)==True
def test_unit_carnumber2():
    carnum="1BC-1243"
    assert Input_car_number(carnum)==False
#輸入車牌錯誤測試(2 fail)
def test_unit_carnumber3():
    carnum="A"
    assert Input_car_number(carnum)==True
def test_unit_carnumber4():
    carnum="Ic8-7630"
    assert Input_car_number(carnum)==True
#停車繳費系統整體測試 (6 pass)      
def test_parking_payment_machine():
    carnumber="ABC-1234"
    five=0
    ten=0
    fifty=0
    fake_5=0
    fake_10=0
    fake_50=0
    test_start=datetime(2023,5,25,23,0)
    test_end=datetime(2023,5,25,23,30)
    test_all=parking_payment_machine(carnumber,five,ten,fifty,fake_5,fake_10,fake_50,test_start,test_end)
    #沒付款OR付款金額不足 回傳false 繳費失敗
    assert test_all==False#平日30分鐘15元 
def test_parking_payment_machine0():
    carnumber="QWE-1234"
    five=1
    ten=1
    fifty=0
    fake_5=0
    fake_10=0
    fake_50=0
    test_start=datetime(2023,5,25,23,0)
    test_end=datetime(2023,5,25,23,30)
    test_all=parking_payment_machine(carnumber,five,ten,fifty,fake_5,fake_10,fake_50,test_start,test_end)
    #繳費成功 
    assert test_all==True#平日30分鐘15元
def test_parking_payment_machine1():
    carnumber="IC8-7630"
    five=1
    ten=1
    fifty=0
    fake_5=0
    fake_10=0
    fake_50=0
    test_start=datetime(2023,5,25,23,0)
    test_end=datetime(2023,5,25,23,30)
    test_all=parking_payment_machine(carnumber,five,ten,fifty,fake_5,fake_10,fake_50,test_start,test_end)
    #繳費成功 
    assert test_all==True#平日30分鐘15元
def test_parking_payment_machine2():
    carnumber="B567-9010"
    five=0
    ten=0
    fifty=7
    fake_5=0
    fake_10=0
    fake_50=0
    test_start=datetime(2023,5,24,23,0)
    test_end=datetime(2023,5,25,23,30)
    test_all=parking_payment_machine(carnumber,five,ten,fifty,fake_5,fake_10,fake_50,test_start,test_end)
    #繳費成功 
    assert test_all==True#跨日計算 第一天(平日) 1H 30元  第二天(平日) 23.5H 300   
def test_parking_payment_machine3():
    carnumber="B5"
    five=0
    ten=0
    fifty=7
    fake_5=0
    fake_10=0
    fake_50=0
    test_start=datetime(2023,5,24,23,0)
    test_end=datetime(2023,5,25,23,30)
    test_all=parking_payment_machine(carnumber,five,ten,fifty,fake_5,fake_10,fake_50,test_start,test_end)
    #查無此車牌 需輸入完整的車牌號碼 繳費失敗
    assert test_all==False
def test_parking_payment_machine4():
    carnumber="B567-9010"
    five=0
    ten=0
    fifty=6
    fake_5=0
    fake_10=0
    fake_50=1
    test_start=datetime(2023,5,24,23,0)
    test_end=datetime(2023,5,25,23,30)
    test_all=parking_payment_machine(carnumber,five,ten,fifty,fake_5,fake_10,fake_50,test_start,test_end)
    #偵測到非法硬幣 回傳false 繳費失敗
    assert test_all==False
#停車繳費系統整體錯誤測試(2 fail)
def test_parking_payment_machine5():
    carnumber="B567-9010"
    five=0
    ten=0
    fifty=6
    fake_5=0
    fake_10=0
    fake_50=1
    test_start=datetime(2023,5,24,23,0)
    test_end=datetime(2023,5,25,23,30)
    test_all=parking_payment_machine(carnumber,five,ten,fifty,fake_5,fake_10,fake_50,test_start,test_end)
    #偵測到非法硬幣 回傳false 繳費失敗
    assert test_all==True
def test_parking_payment_machine6():
    carnumber="B567-9010"
    five=0
    ten=0
    fifty=6
    fake_5=0
    fake_10=0
    fake_50=0
    test_start=datetime(2023,5,24,23,0)
    test_end=datetime(2023,5,25,23,30)
    test_all=parking_payment_machine(carnumber,five,ten,fifty,fake_5,fake_10,fake_50,test_start,test_end)
    #停車費330 user只投入300 回傳false 繳費失敗
    assert test_all==True    

  
